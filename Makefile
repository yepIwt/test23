include .env
export

prepare:
	echo $[FASTAPI_HASH_ALGORITHM]
services:
	echo bringin up services
run:
	echo running up