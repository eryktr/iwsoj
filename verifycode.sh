pytest --cov=iwsoj/tests || flake8 iwsoj
ret=$?

if [ $ret -eq 0 ]; then
  echo "You are good to commit."
else
  echo "Problems exist. Do not commit."
fi

