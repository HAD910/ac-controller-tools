# AC Brotherhood (appid 48190) - tay cam, tiep tu kinh nghiem AC2 (17/11/2026)

## Da xac minh (doc file/log, chua chay game)
- Cai o `Steam\steamapps\common\Assassins Creed Brotherhood` (ACBSP.exe, 32-bit; import XINPUT1_3.dll + DINPUT8.dll giong AC2).
- Steam log: Brotherhood 08:45 17/11 dang dung cau hinh tay cam `controller_base/empty.vdf` (= khong co mapping) -> tay cam khong an.
- Chua co file ini cau hinh nao do Brotherhood tao (khong thay trong Documents/AppData/Local Ubisoft) -> chua toi buoc ghi ini.
  Vi tri thuc su cua ini: CHUA BIET, se biet sau khi game chay toi menu va ghi file.
- `DefaultBindings.map` cua Brotherhood KHONG co muc "Controller (XBOX 360 For Windows)" hay "Xbox One For Windows" (AC2 co).
  Chi co 'Controller (XUSB Gamepad)' (VID 1133/PID 49730): L1=10 L2=4 R1=11 R2=5 StickL/R=8/9 Select/Start=6/7.
  => voi tay Xbox ao cua Steam, Brotherhood co the khong nhan dien -> can them muc ini thu cong (CHUA KIEM CHUNG).
- Tay cam cua nguoi choi dang o che do DS4 gia (BT 054C:09CC), nhung co luc o XInput (3537:100F, va PID moi 3537:1098 - configset cua no dang TRONG, ca AC2 cung chua duoc gan mau).

## Viec da lam
- `tools/py/acb_pad.py` (dry-run mac dinh): them muc 48190 vao cac configset Steam theo mau da chot cho AC2
  (xboxone_ac2_pad cho che do XInput, ps4_ac2_pad cho DS4 gia) va gan luon 33230 cho configset 3537-1098.
  `--apply` chi ghi khi Steam da tat, co backup `backups/steam_controller_<ngay>_acb/`. CHUA --apply (nguoi choi dang choi Syndicate).

## DA --apply (17/11/2026, nguoi choi yeu cau tat Steam): 6 configset da ghi, backup backups/steam_controller_20261117_acb/, Steam da mo lai. CHUA kiem chung trong game.

## INI TIM THAY (17/11 09:30): `%USERPROFILE%\Saved Games\Assassin's Creed Brotherhood\ACBrotherhood.ini` (game tao khi nguoi choi mo no).
- Game thay tay cam la thiet bi tho `[6 axis 14 button device with hat switch]` (VID 1356/PID 2508 = DS4 gia), KHONG qua Steam Input ao.
  SelectedInput van = KeyboardMouse2 -> tay cam chua duoc chon.
- Muc tu sinh co Button1..4 = 0,1,2,3 -> sai thu tu (Button1..4 = A,X,Y,B; DS4 tho Cross=1, Square=0, Triangle=3, Circle=2 -> 1,0,3,2,
  khop muc [Logitech Dual Action] trong DefaultBindings.map). Phan con lai (L1/R1 4/5, L2/R2 6/7, Share/Options 8/9, L3/R3 10/11, stick) hop ly.
- `tools/py/acb_ini.py [--apply]` sua SelectedInput + Button1..4; tu choi ghi khi ACBSP.exe con chay. CHUA ap (nguoi choi dang choi). CHUA kiem chung trong game.

## Lan 2 (17/11, nguoi choi: "khong ok, phai y chang AC2")
- DefaultBindings.map Brotherhood: ca 5 muc tay (Dual Action, RumblePad 2, TWIN SHOCK, XBCD, XUSB) dat Left1/Right1 = CO (LT/RT), Left2/Right2 = bumper.
  Ini game tu sinh cho thiet bi tho dat nguoc (L1=4,L2=6) -> LT/RT va LB/RB bi dao. Da sua: Left1=6 Left2=4 Right1=7 Right2=5
  (= LT khoa muc tieu, RT High Profile, LB camera, RB banh xe vu khi nhu AC2). SUY LUAN tu file mac dinh, CHUA kiem chung trong game.
- Khong lam duoc nhu AC2: L3->Y (Eagle Vision) vi do template Steam; Brotherhood chua qua Steam Input (log: 48190 = 'Local Override' empty.vdf, game thay tay tho).
- Ini bi game ghi de luc thoat (SelectedInput ve KeyboardMouse2) -> sau moi lan choi chay lai `acb_ini.py --apply`.

## 18/11: man hinh game (anh nguoi choi) cho thay Button1=Attack, Button2=Fast walk, Button3=Gentle push, Button4=Eagle vision (=X,A,B,Y theo vi tri Xbox).
- Lan 1 mat da gan Button1..4=1,0,3,2 (SAI); dung la 0,1,2,3 (= gia tri game tu sinh). Da sua + ap. Vai giu 6/4/7/5 (chua kiem chung).
- nguoi choi bao KHONG nut nao an khi ini chon tay cam. Nghi: Steam Input dang bat voi cau hinh RONG cho 48190 ('Local Override' empty.vdf)
  -> pad khong ra gi. Thu: Steam > Brotherhood > Properties > Controller > Disable Steam Input. CHUA kiem chung.

## 18/11 xu ly het (CHUA kiem chung trong game)
- Nguyen nhan 'khong nut nao an': AC2/AC3R co `UseSteamControllerConfig=2` (ep bat Steam Input) trong userdata\<steam_user_id>\config\localconfig.vdf;
  48190 khong co -> Steam dung cau hinh RONG (Override empty.vdf). Da them 3 dong vao khoi "48190" (backup backups/steam_localconfig_20261118/).
- Slot Brotherhood hoan doi tung cap so voi AC2 (Attack = Button2 o AC2, Button1 o ACB; tuong tu Button3<->4, Left1<->Left2, Right1<->Right2)
  -> lan 'vai 6/4/7/5' truoc la SAI huong. acb_ini.py viet lai: SelectedInput = 'Controller (XBOX 360 For Windows)' + muc ao (nut mat 2,0,1,3; vai L1=8 L2=4 R1=9 R2=5),
  muc tho giu lam du phong (nut mat 0,1,2,3, vai 4/6/5/7).
- Steam da bat lai; chua thay log chon template cho 48190 (chi in khi mo game/config) -> can nguoi choi thu.

## 18/11 sua lan cuoi: slot Brotherhood = slot AC2 (KHONG hoan doi)
- nguoi choi: bam LT ra 'chinh cam vao giua' (khi Left2=4) -> Left2 la camera = giong AC2 (LB=camera). Nhan 'Button N' tren man hinh la SO NUT tay cam (gia tri+1),
  khong phai ten slot -> suy luan 'hoan doi cap' o tren la SAI. Phim ban phim (Space=Button1 Fast walk, LMB=Button2 Attack, E=Button3 Eagle) khop thu tu AC2.
- Muc ao [Controller (XBOX 360 For Windows)] nay chep NGUYEN tu AC2 (nut mat 0,2,3,1; vai 4,8,5,9). R3 khong lam gi (nhu AC2: mau Steam bo trong).
- CHUA kiem chung trong game.

## 18/11 chieu: log Steam xac nhan 48190 nhan 'Local Selection Path' = controller_ps4_ac2_pad (pad dang o che do DS4 gia).
- Mau ps4: LT->nut ao 4, LB->8, RB->5, RT->9, L3->Y, R3 trong. nguoi choi: LT phai la High Profile (Left2=camera da xac nhan). Doi: Right1=4 (LT), Left1=9 (RT),
  Left2=8 (LB), Right2=5 (RB). Suy luan: tren tay that Brotherhood, Right1 = RT = High Profile (DefaultBindings XUSB). CHUA kiem chung; chua biet Left1 (RT) lam gi.

## 18/11 toi: nguoi choi sua: High Profile = RT. Ket qua thu (ini Left1=9 Left2=8 Right1=4 Right2=5, mau ps4_ac2): RT -> camera giua, LB -> goc nhin thu nhat, RB -> mo tool, LT -> chua bao.
- Cung mot slot ma khi thi 'camera giua', khi thi 'goc nhin thu nhat' => slot trong ini KHONG quyet dinh (nghi game doc XInput native cho tay Xbox ao;
  AC2 chi dung DirectInput nen can mau hack). Mau ac2_pad doi cho vai (LT->LB ao, RT->R3 ao, LB->L3 ao) => RT ra R3 = camera giua, LB ra L3 = goc nhin thu nhat.
- Doi 48190 sang mau chuan: ps4 -> controller_ps4_gamepad_joystick.vdf, xboxone -> controller_xboxone_gamepad_joystick.vdf (backup backups/steam_controller_20261118_std/).
  Ky vong theo ban phim console chuan: RT=High Profile, LB=camera ngu canh, RB=tool/weapon wheel. CHUA kiem chung. Ini giu nguyen (co the khong con tac dung).

## 18/11 khuya: mau chuan OK (nguoi choi: cac nut khac on). L3 mat tinh nang (Brotherhood khong dung L3 that; AC2 co vi mau hack gan L3 -> Y = Eagle Vision).
- Tao 2 mau moi trong Steam\controller_base\templates: controller_ps4_acb_pad.vdf, controller_xboxone_acb_pad.vdf = ban sao mau chuan,
  chi doi click stick trai 'JOYSTICK_LEFT' -> 'Y'. 48190 tro sang 2 mau nay (backup configset: backups/steam_controller_20261118_acb2/). CHUA kiem chung.
- Go ra: xoa 2 file mau tren + dong "48190" trong cac configset.

## 18/11 khuya (2): nguoi choi muon R3 = goc nhin thu nhat (khong phai camera giua). Thu nghiem truoc: nut ao L3 (JOYSTICK_LEFT) trong Brotherhood = goc nhin thu nhat.
- 2 mau acb_pad: nhom 8 (stick phai) click JOYSTICK_RIGHT -> JOYSTICK_LEFT. Giu: stick trai click -> Y. Nhom 2/6 (trackpad) khong dung. CHUA kiem chung.

## Buoc tiep (cu)
1. (xong) tat Steam -> acb_pad.py --apply -> mo lai Steam.
2. Chay Brotherhood toi menu 1 lan (cho game tao ini) -> tim file ini moi, xem muc [Input] SelectedInput + section Controller.
3. Neu section cua tay chua co: them theo mau AC2 `[Controller (XBOX 360 For Windows)]` (can phai 132/133, LT/RT = nut 8/9, Select/Start 6/7),
   nhung doi chieu nut Brotherhood trong DefaultBindings (L1/L2 co the dao).
4. Bo cuc Brotherhood khac AC2: them goi sat thu (call assassins), nang cap thanh, crossbow/sung - can xem lai trong game, dung mau AC2 lam goc.
