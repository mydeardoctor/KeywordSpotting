# Build docker image.
docker build --tag img_kws_jupyter_server .

# Run docker container.
docker run `
--gpus all `
--interactive `
--name con_kws_jupyter_server `
--publish 127.0.0.1:8888:8888 `
--tty `
img_kws_jupyter_server