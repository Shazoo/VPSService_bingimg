0 6 * * * /cd /srv/bing-img ;srv/bing-img/venv/bin/python /srv/bing-img/bing_img.py >> /srv/bing-img/img_list.txt; git add img_list.txt; git commit -m 'update'; git push origin master
