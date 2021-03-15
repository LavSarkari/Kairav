git reset --hard && git pull



rm -r "/data/data/com.termux/files/usr/share/Kairav"
rm "/data/data/com.termux/files/usr/bin/Kairav"

echo -e "$red [$green+$red]$off Updating ...";
mkdir "/data/data/com.termux/files/usr/share/Kairav"
 cp "Kairav.py" "/data/data/com.termux/files/usr/share/Kairav"
 cp "install.sh" "/data/data/com.termux/files/usr/share/Kairav"
 cp -R "utility/" "/data/data/com.termux/files/usr/share/Kairav/modules"
 cp -R "modules/"  "/data/data/com.termux/files/usr/share/Kairav/core"
 echo -e "$red [$green+$red]$off Creating Symbolic Link ...";
 echo "#!/data/data/com.termux/files/usr/bin/bash
python3 /data/data/com.termux/files/usr/share/Kairav/Kairav.py" '${1+"$@"}' > "Kairav";
 cp "Kairav" "/data/data/com.termux/files/usr/bin"
 chmod +x "/data/data/com.termux/files/usr/bin/Kairav"
 rm "Kairav";
 if [ -d "/data/data/com.termux/files/usr/share/Kairav" ] ;
then
echo -e "$red [$green+$red]$off Tool successfully Updated and will start in 7s!";
echo -e "$red [$green+$red]$off You can execute tool by typing Kairav"
sleep 7;
Kairav
else
echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
fi
}
