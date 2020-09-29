import uuid
from django.shortcuts import render
from django.http import Http404
from subs import models, serializers
from rest_framework import viewsets


def subs(request, group_id):
    try:
        subscriptions = models.Subscriptions.objects.filter(group=group_id)
    except:
        raise Http404("Нет подписок на группу")

    group = subscriptions[0].group
    admins = [subscription.person for subscription in subscriptions if subscription.admin]
    members = [subscription.person for subscription in subscriptions]
    persons_to_add = models.Persons.objects.all()
    # if request.method == "POST" and request.POST.get("selectplace"):
    #     sub_info = models.Subscriptions(subscription = name, person = description, group = genre_id, admin = country)
    #     film_info.save()
    #     client = request.POST.get("client")
    #     pls = request.POST.get("selectplace").split(" ")[:-1]
    #     for pl in pls:
    #         id = pl[5:]
    #         if pl[5:6] == "0":
    #             id = pl[6:]
    #         field = Places.objects.get(placeid = id)
    #         field.clientname = client
    #         field.state = "Занято"
    #         field.save()

    return render(request, 'subs/subs.html', locals())


# class PersonsView(APIView):
#     @staticmethod
#     def get(request):
#         persons = models.Persons.objects.all()
#         serializer = serializers.PersonsSerializer(persons, many=True)
#         return Response({"persons": serializer.data})
#
#     @staticmethod
#     def post(request):
#         person = request.data.get('person')
#         serializer = serializers.PersonsSerializer(data=person)
#         if serializer.is_valid(raise_exception=True):
#             created_person = serializer.save()
#         return Response({
#             "success": "Person '{} {}' created successfully".format(created_person.first_name, created_person.last_name)
#         })
#
#     @staticmethod
#     def put(request, person_id):
#         serializer = serializers.PersonsSerializer(
#             instance=get_object_or_404(models.Persons.objects.all(), person=person_id),
#             data=request.data.get('person'),
#             partial=True
#         )
#         if serializer.is_valid(raise_exception=True):
#             updated_person = serializer.save()
#         return Response({
#             "success": "Person '{} {}' updated successfully".format(updated_person.first_name, updated_person.last_name)
#         })
#
#     @staticmethod
#     def delete(request, person_id):
#         get_object_or_404(models.Persons.objects.all(), person=person_id).delete()
#         return Response({"message": "Person with id `{}` has been deleted.".format(person_id)}, status=204)


# @api_view(['GET', 'POST'])
# def person_list(request):
#     if request.method == 'GET':
#         persons = models.Persons.objects.all()
#         serializer = serializers.PersonsSerializer(persons, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = serializers.PersonsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def person_detail(request, person_id):
#     try:
#         person = models.Persons.objects.get(person=person_id)
#     except models.Persons.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         return Response(serializers.PersonsSerializer(person).data)
#
#     elif request.method == 'PUT':
#         serializer = serializers.PersonsSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         person.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# class PersonsViewSet(viewsets.ModelViewSet):
#     queryset = models.Persons.objects.all()
#     serializer_class = serializers.PersonsSerializer
