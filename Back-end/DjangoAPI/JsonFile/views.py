from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from JsonFile.serializers import UserSerializer,JsonfileSerializer
from JsonFile.models import User,JsonfileModel


# Create your views here.
@csrf_exempt
def UserApi(request,login=''):
    if request.method == 'GET':
        user = User.objects.all() # in order to convert it to JSON format
        user_serializer = UserSerializer(user,many=True)
        return JsonResponse(user_serializer.data,safe = False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully !!", safe = False)
        return JsonResponse("Failet to Add !!", safe = False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(Login=user_data['Login'])
        user_serializer = UserSerializer(user,data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully !!", safe = False)
        return JsonResponse("Failed to Update !!", safe = False)
    elif request.method == 'DELETE':
        user = User.objects.get(Login=login)
        user.delete()
        return JsonResponse("Deleted Successfully" , safe = False)


@csrf_exempt
def JsonfileApi(request,name=''):
    if request.method == 'GET':
        Data = JsonfileModel.objects.all() # in order to convert it to JSON format
        Jsonfile_serializer = JsonfileSerializer(Data,many=True)
        return JsonResponse(Jsonfile_serializer.data,safe = False)
    elif request.method == 'POST':
        Jsonfile_data = JSONParser().parse(request)
        Jsonfile_serializer = JsonfileSerializer(data=Jsonfile_data)
        if Jsonfile_serializer.is_valid():
            Jsonfile_serializer.save()
            return JsonResponse("Added Successfully !!", safe = False)
        return JsonResponse("Failet to Add !!", safe = False)
    elif request.method == 'PUT':
        Jsonfile_data = JSONParser().parse(request)
        Jsonfile = JsonfileModel.objects.get(Name=Jsonfile_data['Name'])
        Jsonfile_serializer = JsonfileSerializer(Jsonfile,data = Jsonfile_data)
        if Jsonfile_serializer.is_valid():
            Jsonfile_serializer.save()
            return JsonResponse("Updated Successfully !!", safe = False)
        return JsonResponse("Failed to Update !!", safe = False)
    elif request.method == 'DELETE':
        Jsonfile = JsonfileModel.objects.get(Name=Name)
        Jsonfile.delete()
        return JsonResponse("Deleted Successfully" , safe = False)

# first_file = Jsonfile(Name = 'data.json' , Details = {
# "tokenRange": {
#     "keyAlias": "123457960000000000000",
#     "accountRangeFrom": "1234579600000000085",
#     "accountRangeTo": "1234579600000000095"
# },
# "billingICA": "1122",
# "customerName": "Fifth Third Bank, The",
# "floorExpiryDate": "1220",
# "keyDerivationIndex": "001" ,
# "emvData": {
#     "bin": "12345796",
#     "issuerKeyExpiryDate": "1221",
#     "paymentSystemKeyIndex": "05",
#     "issuerKeySize": "1408",
#     "issuerKeyAlgorithmIndicator": "01"
# },
# "imkAcXtraData": {
#     "invalidCryptogram": "008",
#     "notValidateCryptogram": "001",
#     "invalidTvrCvr": "005",
#     "cryptogramNotArqc": "004",
#     "atcOutsideRange": "005",
#     "atcReplay": "005",
#     "height": "00",
#     "branch": "00",
#     "derivationAlgorithmId": "1",
#     "cardApplicationIdentifier": "1",
#     "arqcArpcAlgorithmId": "1",
#     "cvnPositionIndicator": "1",
#     "arpcRespIfTransactionAccepted": "00000000",
#     "arpcRespIfTransactionRejected": "00000000",
#     "tvrBitmask": "0000A80000",
#     "tvrExpected": "0000000000",
#     "cvrBitmask": "000240000000",
#     "cvrExpected": "000240000000",
#     "posEntryMode": "09",
#     "atcHighRange": "00020",
#     "atcLowRange": "00999"
# },
# "imkCvc3XtraData": {
#     "invalidCvc3": "008",
#     "notValidateCvc3": "005",
#     "allowedAtcRange": "008",
#     "numberMismatch": "004",
#     "algorithmId": "1",
#     "pCvc3Track1": "00000000070000",
#     "pUnAtcTrack1": "01fc0000000000",
#     "nUnTrack1": "04",
#     "ppseqTrack1": "00000000800000",
#     "pCvc3Track2": "00E0",
#     "pUnAtcTrack2": "0F1E",
#     "nUnTrack2": "04",
#     "ppseqTrack2": "1000",
#     "cvc3AlgoId": "1",
#     "highestATC": "00140",
#     "lowestATC": "00050"
# },
# "imkAcvcclXtraData": {
#     "invalidMdAcAndUmdAc": "008",
#     "validMdAndInvalidUmdAc": "008",
#     "invalidMdAndValidUmdAc": "001",
#     "tokenSuspension": "012",
#     "notValidateCryptogram": "004",
#     "invalidTvrCvr": "005",
#     "numberMismatch": "000",
#     "invalidAtc": "005",
#     "atcReplay": "005",
#     "derivationAlgorithmId": "4",
#     "cardApplicationIdentifier": "4",
#     "arqcAlgorithmId": "1",
#     "cvnPositionIndicator": "1",
#     "arpcRespIfTransAccepted": "00110000",
#     "arpcRespIfTransRejected": "00120000",
#     "tvrBitmask": "0000200000",
#     "tvrExpected": "0000000000",
#     "cvrBitmask": "000000890008",
#     "cvrExpected": "000000000000",
#     "arqc1Mask": "11000000",
#     "arqc2Mask": "00000001",
#     "pCvc3Track1": "000000000000F0",
#     "pUnAtcTrack1": "00000000000F0E",
#     "nUnTrack1": "03",
#     "ppseqTrack1": "00000000001000",
#     "pCvc3Track2": "00F0",
#     "pUnAtcTrack2": "0F0E",
#     "nUnTrack2": "03",
#     "ppseqTrack2": "1000",
#     "cvc3AlgoId": "1"
# },
# "imkAcrpXtraData": {
#     "invalidMdAcAndUmdAc": "005",
#     "validMdAndInvalidUmdAc": "005",
#     "invalidMdAndValidUmdAc": "008",
#     "tokenSuspension": "005",
#     "notValidateCryptogram": "005",
#     "invalidTvrCvr": "005",
#     "numberMismatch": "005",
#     "invalidAtc": "005",
#     "atcReplay": "005",
#     "derivationAlgorithmId": "4",
#     "cardApplicationIdentifier": "4",
#     "arqcAlgorithmId": "1",
#     "cvnPositionIndicator": "1",
#     "arpcRespIfTransAccepted": "00100000",
#     "arpcRespIfTransRejected": "00000000",
#     "tvrBitmask": "A800000000",
#     "tvrExpected": "0000000000",
#     "cvrBitmask": "000000890008",
#     "cvrExpected": "000000000000",
#     "arqc1Mask": "11110000",
#     "arqc2Mask": "00000000"
# }
# })
# first_file.save()   just to be runned as a single time
