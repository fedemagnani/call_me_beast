# Requirements
Install docker for ubuntu here https://docs.docker.com/engine/install/ubuntu/


# Steps

- Create `src` app in the parent folder
- in the parent folder, create the `Dockerfile`
- in the `src` folder, create the `app.py` file
- in the parent folder build the docker image using a reusable tag_name: `sudo docker build --tag <tag_name> .`. Here we are using `call_me_beast`, so the command is 
```
sudo docker build --tag call_me_beast .
``` 
- we create an output directory> the name of the output directory will be the same of the env OUTPUT_DIR. This will create a folder in `computer/tmp/output_lilypad`
```
mkdir /tmp/output_lilypad
```
- in order to run locally the application, we run 
```
sudo docker run --rm -v /tmp/output:/output_lily -e OUTPUT_DIR=/output_lily call_me_beast --x 1 --
y 8
``` 
The expected output is 9. results are going to be saved in `computer/tmp/output_lilypad`. Notice in fact that via the `-e` tag we are setting the environment variable, while with `-v` we are creating a sort of remapping (`output_lily` in the docker container is mapped to the local folder of the device `/tmp/output_lilypad`)
- Now we are about to push the image to dockerhub, so we run 
```
sudo docker login
```
- Once that the login is perfomed, we associate the tag initially defined via `docker tag <tag_name> <docker-hub-user>/<tag_name>:1.0.0`. In our case is
```
sudo docker tag call_me_beast drunnn/call_me_beast:1.0.0
```
- Now we are ready to push the image to dockerhub
```
sudo docker push drunnn/call_me_beast:1.0.0
```
- In order to recover the sha256 digest of the pushed image, one can run (notice that we are replacing `sha256:` with `0x`)
`docker pull <docker-hub-user>/<tag_name>:1.0.0 | grep "Digest: sha256:" | sed 's/.*sha256:/0x/'` i.e.
```
sudo docker pull drunnn/call_me_beast:1.0.0 | grep "Digest: sha256:" | sed 's/.*sha256:/0x/'
```
- Now we need to create the `lilypad_module.json.tmpl` file (check example file). Make sure it is called in this way
- Once that we have pushed our repo, you need to create a tag for the code on github. We are calling it `v1.2`. NOw we are ready to run our job task. Notice that `--module-hash` refers to the commit hash of the update
```
lilypad run github.com/fedemagnani/call_me_beast:v1.2 -i X=5 -i Y=3 --module-repo https://github.com/fedemagnani/call_me_beast --module-hash 5e477712394cb29cebf68aa2ac1b8b63f9e9cf01 --module-path ./lilypad_module.json.tmpl
```

If you want more verbose logs, tyoe `export LOG_LEVEL=debug`