"""Chinh ini tay cam AC Brotherhood cho GIONG AC2 (di qua Steam Input -> tay Xbox 360 ao, mau controller_*_ac2_pad.vdf).

  python tools/py/acb_ini.py            # dry-run
  python tools/py/acb_ini.py --apply    # ghi (phai THOAT Brotherhood truoc: game ghi de ini luc thoat). Backup: backups/acb_ini_<ngay>/

ini: %USERPROFILE%\\Saved Games\\Assassin's Creed Brotherhood\\ACBrotherhood.ini
Dat SelectedInput = 'Controller (XBOX 360 For Windows)' (Valve 28DE:11FF, giong AC2) va tao/ghi de muc do.

Slot Brotherhood = slot AC2 (Button1 Fast walk, Button2 Attack, Button3 Eagle vision, Button4 Gentle push; xac nhan 18/11 bang so nut tren man hinh
game + phim ban phim; nhan 'Button N' tren man hinh la SO NUT tay cam, khong phai ten slot). LT bam ra 'chinh cam' khi dung Left2 -> Left2 = camera.
=> muc ao CHEP NGUYEN tu muc [Controller (XBOX 360 For Windows)] cua AC2 (Left1=4 Left2=8 Right1=5 Right2=9, nut mat 0,2,3,1).
Mau Steam (controller_xboxone_ac2_pad): LT->ao nut 4, RT->5, LB->8, RB->9, L3->Y, R3 khong lam gi (nhu AC2).
Muc thiet bi tho [6 axis 14 button device with hat switch] (du phong neu Steam Input khong bat): nut mat 0,1,2,3, vai 4/6/5/7 (game tu sinh).
"""
import datetime, os, re, shutil, subprocess, sys

INI = os.path.join(os.environ["USERPROFILE"], "Saved Games", "Assassin's Creed Brotherhood", "ACBrotherhood.ini")
VIRT = "Controller (XBOX 360 For Windows)"
VIRT_BODY = """VendorID=10462
ProductID=4607
Button1=0
Button2=2
Button3=3
Button4=1
PadUp=64
PadRight=65
PadDown=66
PadLeft=67
Select=6
Start=7
ShoulderLeft1=9
ShoulderLeft2=8
ShoulderRight1=4
ShoulderRight2=5
StickLeft=12
StickRight=13
LeftStickUp=130
LeftStickDown=130
LeftStickLeft=129
LeftStickRight=129
RightStickUp=133
RightStickDown=133
RightStickLeft=132
RightStickRight=132"""
RAW = "6 axis 14 button device with hat switch"
RAW_WANT = {"Button1": "0", "Button2": "1", "Button3": "2", "Button4": "3",
            "ShoulderLeft1": "4", "ShoulderLeft2": "6", "ShoulderRight1": "5", "ShoulderRight2": "7"}


def running():
    return "acbsp.exe" in subprocess.run(["tasklist", "/FI", "IMAGENAME eq ACBSP.exe", "/NH"], capture_output=True, text=True).stdout.lower()


def main():
    raw = open(INI, encoding="utf-8", newline="").read()
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.replace("\r\n", "\n").split("\n")
    # tach thanh cac muc
    secs, order, cur = {}, [], None
    pre = []
    for l in lines:
        m = re.match(r"\[(.+)\]\s*$", l)
        if m:
            cur = m.group(1); order.append(cur); secs[cur] = []
        elif cur is None:
            pre.append(l)
        else:
            secs[cur].append(l)
    changed = []
    # SelectedInput
    for i, l in enumerate(secs.get("Input", [])):
        if l.startswith("SelectedInput=") and l != "SelectedInput=" + VIRT:
            changed.append("SelectedInput: %s -> %s" % (l.split("=", 1)[1], VIRT)); secs["Input"][i] = "SelectedInput=" + VIRT
    # muc ao
    want = VIRT_BODY.split("\n")
    if VIRT not in secs:
        order.append(VIRT); secs[VIRT] = want + [""]; changed.append("them muc [%s]" % VIRT)
    else:
        body = [x for x in secs[VIRT] if x.strip()]
        if body != want:
            secs[VIRT] = want + [""]; changed.append("ghi lai muc [%s]" % VIRT)
    # muc tho (du phong)
    if RAW in secs:
        for i, l in enumerate(secs[RAW]):
            kv = re.match(r"(\w+)=(.*)$", l)
            if kv and kv.group(1) in RAW_WANT and kv.group(2) != RAW_WANT[kv.group(1)]:
                changed.append("[raw] %s: %s -> %s" % (kv.group(1), kv.group(2), RAW_WANT[kv.group(1)]))
                secs[RAW][i] = "%s=%s" % (kv.group(1), RAW_WANT[kv.group(1)])
    print("\n".join(changed) or "Khong co gi can sua.")
    if not changed or "--apply" not in sys.argv: return 0
    if running():
        print("ACBSP.exe dang chay -> TU CHOI (game se ghi de ini khi thoat). Thoat game roi chay lai."); return 2
    b = os.path.join(os.path.dirname(__file__), "..", "..", "backups", "acb_ini_%s" % datetime.date.today().strftime("%Y%m%d"))
    os.makedirs(b, exist_ok=True)
    dst = os.path.join(b, "ACBrotherhood.ini")
    if not os.path.exists(dst): shutil.copy2(INI, dst)      # khong de ban goc cua ngay
    else: shutil.copy2(INI, os.path.join(b, "ACBrotherhood.%s.ini" % datetime.datetime.now().strftime("%H%M%S")))
    out = list(pre)
    for s in order:
        out.append("[%s]" % s); out += secs[s]
    text = nl.join(out).rstrip("\n") + nl
    open(INI, "w", encoding="utf-8", newline="").write(text)
    print("DA GHI. Backup:", os.path.abspath(b)); return 0


if __name__ == "__main__":
    sys.exit(main())
