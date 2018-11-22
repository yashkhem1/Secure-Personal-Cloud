if [[ $1 == "en" ]]; then
	if [[ $2 == "AES" ]]; then
		echo "$2" "en"
		openssl enc -a -aes-256-ecb -in "$4" -out "$5" -K "$3" -A
		# openssl enc -a -in "$5" -out "$5"".1"
		#statements
	fi
	if [[ $2 == "DES" ]]; then
		openssl enc -a -des-ede3-ecb -in "$4" -out "$5" -K "$3" -A
		# openssl enc -a "$5"
		#statements
	fi
	# if [[ $2=="" ]]; then
	# 	#statements
	# fi
	#statements
elif [[ $1 == "de" ]]; then
	if [[ $2 == "AES" ]]; then
		echo "$2" "de"
		openssl enc -d -a -aes-256-ecb -in "$4" -out "$5" -K "$3" -A
		#statements
	fi
	if [[ $2 == "DES" ]]; then
		openssl enc -d -aA -des-ede3-ecb -in "$4" -out "$5" -K "$3" -A
		#statements
	fi
fi

