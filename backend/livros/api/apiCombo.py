from ninja import Router
from django.http import JsonResponse
from django.db.models import Q
from typing import List
from ..models import Combo
from datetime import datetime, timedelta
from ..schemas import ComboSchema

combos_router = Router()

@combos_router.get('todosCombos/', response=List[ComboSchema])
def getTodosCombos(request):
    combos = Combo.objects.all()

    if combos.exists():
        return combos
    else:
        JsonResponse({'msg':'Nenhum combo foi encontrado'})
