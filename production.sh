echo "** Compiling ."
cd webapp;
npm run build;

echo "*** Moving .."
cd ../app_backend/frontapp;
rm -rf *;
cp -r ../../webapp/dist/* ./;

echo "**** Uploading to Heroku ..."
cd ../;
git add .
git commit -m "feat: deploy";
git push heroku master;

echo "***** Finishing ..."
