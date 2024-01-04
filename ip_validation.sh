# 6 kyu kata

adr="$1"
regex='(\b25[0-5]|\b2[0-4][0-9]|\b[1]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)){3}'

if [[ $adr =~ $regex ]]
then 
  echo "True"
else
  echo "False"
fi
