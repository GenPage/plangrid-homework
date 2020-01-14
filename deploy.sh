#!/bin/bash

function ssh_cmd () {
	ssh interview@184.73.85.204 "$1"  
}


ssh_cmd 'sudo docker stop homework'
ssh_cmd 'sudo docker run --rm -d -p 8000:8000 --name="homework" genpage/plangrid-homework'


