"""Dang ky cau hinh tay cam (Steam Input) cho AC Brotherhood (appid 48190) giong AC2 (33230).

Cach dung:
  python tools/py/acb_pad.py            # dry-run: chi in ra se sua gi
  python tools/py/acb_pad.py --apply    # ghi that (can Steam DA TAT: steam.exe -shutdown)

Quy tac: moi configset da co muc 33230 -> them muc 48190 cung template.
Rieng configset trong (vd 3537-1098-... = che do XInput moi cua GameSir) -> them CA 33230 va 48190
voi controller_xboxone_ac2_pad.vdf. Backup truoc khi ghi: backups/steam_controller_<ngay>_acb/.
Muc 'template' lay tu thu muc Steam\\controller_base\\templates (mau AC2 da dung san).
"""
import os, re, shutil, subprocess, sys, datetime

CFG = r"C:\Program Files (x86)\Steam\steamapps\common\Steam Controller Configs\<steam_user_id>\config"
TPL = r"C:\Program Files (x86)\Steam\controller_base\templates"
BACKUP_ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "backups")
AC2, ACB = "33230", "48190"
XBOX_TPL = "controller_xboxone_ac2_pad.vdf"


def steam_running():
    out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq steam.exe", "/NH"], capture_output=True, text=True).stdout
    return "steam.exe" in out.lower()


def block(appid, tpl):
    return '\t"%s"\n\t{\n\t\t"template"\t\t"%s"\n\t}\n' % (appid, tpl)


def plan(path):
    """Tra ve (text_moi, ghi_chu) hoac (None, ly_do)."""
    text = open(path, encoding="utf-8", newline="").read()
    nl = "\r\n" if "\r\n" in text else "\n"
    t = text.replace("\r\n", "\n")
    if '"%s"' % ACB in t:
        return None, "da co %s" % ACB
    m = re.search(r'"%s"\s*\{\s*"template"\s*"([^"]+)"' % AC2, t)
    add = ""
    if m:
        add = block(ACB, m.group(1))
        note = "them %s -> %s (theo %s)" % (ACB, m.group(1), AC2)
    elif re.search(r'"controller_config"\s*\{\s*\}', t):
        add = block(AC2, XBOX_TPL) + block(ACB, XBOX_TPL)
        note = "configset trong: them %s va %s -> %s" % (AC2, ACB, XBOX_TPL)
    else:
        return None, "khong co %s va khong rong - bo qua (xem tay)" % AC2
    i = t.rstrip().rfind("}")
    new = t[:i] + add + t[i:]
    return new.replace("\n", nl), note


def main():
    apply = "--apply" in sys.argv
    for f in (XBOX_TPL, "controller_ps4_ac2_pad.vdf"):
        if not os.path.exists(os.path.join(TPL, f)):
            print("THIEU mau Steam:", f); return 1
    keep = ("3537-", "3735a9ea0b8b", "45e-2ff", "controller_ps4", "controller_xboxone")
    files = sorted(f for f in os.listdir(CFG) if f.startswith("configset_") and f.endswith(".vdf")
                   and any(k in f for k in keep))
    todo = []
    for f in files:
        p = os.path.join(CFG, f)
        new, note = plan(p)
        print("%-52s %s" % (f, note))
        if new is not None:
            todo.append((p, new))
    if not todo:
        print("Khong co gi can sua."); return 0
    if not apply:
        print("\n(dry-run) them --apply de ghi; nho tat Steam truoc."); return 0
    if steam_running():
        print("\nSteam dang chay -> TU CHOI ghi (Steam se ghi de). Chay: steam.exe -shutdown"); return 2
    bdir = os.path.join(BACKUP_ROOT, "steam_controller_%s_acb" % datetime.date.today().strftime("%Y%m%d"))
    os.makedirs(bdir, exist_ok=True)
    for p, new in todo:
        shutil.copy2(p, os.path.join(bdir, os.path.basename(p)))
        with open(p, "w", encoding="utf-8", newline="") as fh:
            fh.write(new)
        print("DA GHI", os.path.basename(p))
    print("Backup:", os.path.abspath(bdir))
    return 0


if __name__ == "__main__":
    sys.exit(main())
