## Exercise 2.3 Overview


mkdir ~/environment/car3
cd ~/environment/car3
aws iot create-thing --thing-name car3
aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.pem.crt --private-key-outfile private.pem.key

This command will place the Certificate and Private Key in the certificate.pem.crt file and private.pem.key respectively. It will also output the certificateArn which you will re-use in the next command.
To attach the Policy to the Certificate, enter the following command. Replace certificateArn_changeme with the value of the attribute certificateArn from the output of the previous command. It should be similar to: arn:aws:iot:us-east-1:1234567890:cert/0f11db22dafacda87be0940dd5b2e010635916f541461ccf2d1c56ced0f343ee

arn:aws:iot:us-east-1:010703111265:cert/8031c5c130fe033706f36721aae15620101315af3a7f8c877b10ce52a6a05e10
aws iot attach-policy --policy-name labPolicy --target certificateArn_changeme

-> aws iot attach-policy --policy-name CarPolicy --target arn:aws:iot:us-east-1:010703111265:cert/8031c5c130fe033706f36721aae15620101315af3a7f8c877b10ce52a6a05e10

-> aws iot attach-thing-principal --thing-name car3 --principal arn:aws:iot:us-east-1:010703111265:cert/8031c5c130fe033706f36721aae15620101315af3a7f8c877b10ce52a6a05e10

mkdir ~/environment/car4
cd ~/environment/car4
aws iot create-thing --thing-name car4
aws iot create-keys-and-certificate --set-as-active --certificate-pem-outfile certificate.pem.crt --private-key-outfile private.pem.key

arn:aws:iot:us-east-1:010703111265:cert/99a8e077e257527f4aef75b25c7668ceef147073ed9889ba22b643c1314144c7

-> aws iot attach-policy --policy-name CarPolicy --target arn:aws:iot:us-east-1:010703111265:cert/99a8e077e257527f4aef75b25c7668ceef147073ed9889ba22b643c1314144c7

-> aws iot attach-thing-principal --thing-name car4 --principal arn:aws:iot:us-east-1:010703111265:cert/99a8e077e257527f4aef75b25c7668ceef147073ed9889ba22b643c1314144c7

 cp ~/environment/car1/exercise-2.3.py ~/environment/car4
 cp ~/environment/car1/exercise-2.3.py ~/environment/car3


 python exercise-2.3.py