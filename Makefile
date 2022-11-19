include .env
export

prepare:
	echo bringin up services
services:
	echo ${FASTAPI_HASH_ALGORITHM}
run:
	echo ${FASTAPI_HASH_ALGORITHM}