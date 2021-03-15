red="\e[0;31m"
green="\e[0;32m"
off="\e[0m"
figlet Kairav
echo Installing...

function termux() {
  echo -e "$red [$green+$red]$off Installing Python ...";
pkg install -y python*
echo -e "$red [$green+$red]$off Installing Requirements ...";
pip3 install -r requirements.txt

  echo -e "$red [$green+$red]$off Checking directories ..."

if [ -e "/data/data/com.termux/files/usr/share/Kairav" ]; then
  echo -e "$red [$green+$red]$off A previous installation was found Do you want to replace it? [Y/n]: "
read replace
if [ "$replace" == "y" ] || [ "$replace" == "Y" ] || [ -z "$replace" ]; then
 rm -r "/data/data/com.termux/files/usr/share/Kairav"
 rm "/data/data/com.termux/files/usr/bin/Kairav"
else
  echo -e "$red [$green✘$red]$off If You Want To Install You Must Remove Previous Installations";
  echo -e "$red [$green✘$red]$off Installation Failed";
 exit
fi
fi

  echo -e "$red [$green+$red]$off Installing ...";
mkdir "/data/data/com.termux/files/usr/share/Kairav"
 cp "Kairav.py" "/data/data/com.termux/files/usr/share/Kairav"
 cp "install.sh" "/data/data/com.termux/files/usr/share/Kairav"
 cp "update.sh" "/data/data/com.termux/files/usr/share/Kairav"
 cp -R "modules/" "/data/data/com.termux/files/usr/share/Kairav/modules"
 cp -R "core/"  "/data/data/com.termux/files/usr/share/Kairav/core"
  echo -e "$red [$green+$red]$off Creating Symbolic Link ...";
  echo "#!/data/data/com.termux/files/usr/bin/bash
python3 /data/data/com.termux/files/usr/share/Kairav/Kairav.py" '${1+"$@"}' > "Kairav";
 cp "Kairav" "/data/data/com.termux/files/usr/bin"
 chmod +x "/data/data/com.termux/files/usr/bin/Kairav"
 rm "Kairav";
 if [ -d "/data/data/com.termux/files/usr/share/Kairav" ] ;
then
echo -e "$red [$green+$red]$off Tool successfully installed and will start in 7s!";
echo -e "$red [$green+$red]$off You can execute tool by typing Kairav"
sleep 7;
Kairav
else
echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
fi
}
termux
