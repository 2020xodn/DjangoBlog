# views.py 에서 사용하는 공용 함수를 모아놓은 파일

def canDelete(request):
    for values in request.user.groups.values_list():    # group에 Manager가 있을 경우 True 반환
        if values[1] == 'Manager':
            return True
    else:
        return False

