#!/usr/bin/bash

export ALLMSS="A25 A116 A336 Bas Base La2 La35 LaSM M118 M136 P01 Pal Patm S249 Sin V1639 V1920"
export TESTMSS="A25 A116 Base"

for i in $TESTMSS
do
	export MS=$i
	DocDir="TLGC_2062_006_"$MS"_B01"
	echo $DocDir
	if [ -d "$DocDir" ]; then
		rm -r -f $DocDir
	fi
	mkdir $DocDir
	echo $DocDir"/metadata.json"
	export ID="TLGC_2062_06_"
	export ID="${ID}$MS"
	export ID="${ID}_B01"
	cat >$DocDir/metadata.json <<EOF
{
	"_id" : "$ID",
	"siglum" : "$MS"
}
EOF
done
