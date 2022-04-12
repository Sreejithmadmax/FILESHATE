if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Sreejithmadmax/FILESHATE.git /FILESHATE
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /FILESHATE
fi
cd /LuciferMoringstar-Robot
pip3 install -U -r requirements.txt
echo "Starting FILESHATE...."
python3 main.py
