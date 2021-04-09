Recommends Api
========================

Endpoints:
-------------------------

1. **/recommendations**

Method: GET 

Params: 
- sku (required) имя товара для которого нужно получить рекомендации
- min_rank (optional) минимальный порог близости для рекомендаций

Example request: http://0.0.0.0:8080/recommendations?sku=F3kzjEd4Gi&min_rank=0.8

Example response:
{
    "recommendations": [
        "0LGxtJDY0f",
        "1RKxQK4kqt",
        "47cT30naTF",
        "6NUcom5mRd",
        "6fUjqNSEvx",
        "9t1ic3UWxr",
        "Gs3RgXZNWg",
        "IQ3uxSAp9N",
        "K2vOqSPF9n",
        "NMVEQEznnG",
        "P8azkz3neW",
        "RjzmdSF2vF",
        "VQidQDx6Us",
        "VZGqpulgvH",
        "ZRzDh2ngTX",
        "a79A6WMS9k",
        "dfvLy4sWrO",
        "jMJsXWEZou",
        "nscFcpx9Ix"
    ],
    "err": null
}



Запуск 
-------------------------

#### с Docker
Разархивировать архив recommends в папку проекта 

docker build -t docker-recommends-api .

docker run --name api-container -p8080:8080 docker-recommends-api

#### Без Docker
Разархивировать архив recommends в папку проекта 

python app.py

Info
-------------------------
Получение рекомендаций осуществляется с помощью бинарного поиска в предварительно отсортированном в алфавитном порядке с учетом регистра csv файле

