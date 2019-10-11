pytest ./iwsoj --cov=iwsoj --cov-config=./iwsoj/.coveragerc || flake8 iwsoj
ret=$?

if [ $ret -eq 0 ]; then
  echo "You are good to commit."
else
  echo "Problems exist. Do not commit."
fi

