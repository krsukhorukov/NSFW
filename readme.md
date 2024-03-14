
# Проверка на цензуру
[Below in English](#Censorship Check)
*Проект представляет собой простой API на основе FastAPI для классификации изображений на наличие неприемлемого контента (NSFW - Not Safe For Work).*

### Установка
1. Клонируйте репозиторий:
`git clone https://github.com/krsukhorukov/NSFW.git
2.  Перейдите в каталог проекта:
`cd your_repository`
3. Установите зависимости:
`pip install -r requirements.txt`

### Запуск
*Для запуска API выполните команду:*
`uvicorn main:app --reload`
API будет доступно по адресу http://127.0.0.1:8000.

### Использование
#### 1. Загрузка изображения для классификации
Отправьте POST-запрос на /classify, прикрепив изображение в форме данных. Формат изображения должен быть поддерживаемым (например, JPEG, PNG).

**Пример использования с помощью curl:**
	> curl -X 'POST' \
	  'http://127.0.0.1:8000/classify' \
	  -H 'accept: application/json' \
	  -H 'Content-Type: multipart/form-data' \
	  -F 'file=@"/path/to/your/image.jpg"'  -F 'file=@"/path/to/your/image.jpg"'

#### 2. Получение результата
API вернет результат классификации изображения в виде JSON-ответа. Возможные значения результата: "Censored" (цензурировано) или "Not Censored" (не цензурировано).
**Пример JSON-ответа:**

> {
  "result": "Censored"
}

###Описание методов

##### GET /
Возвращает приветственное сообщение.

##### POST /classify
Принимает изображение для классификации. Возвращает результат классификации в виде JSON-ответа.

### Примечания
- Классификация изображений осуществляется с использованием модели NSFW Image Detection, обученной на основе трансформеров.

- Временные файлы изображений сохраняются в каталоге temp и удаляются после обработки.

- Если формат файла не является изображением или возникают ошибки при обработке, API возвращает соответствующие HTTP-статусы и детали ошибок.

### Censorship Check
*This project is a simple FastAPI-based API for classifying images for inappropriate content (NSFW - Not Safe For Work).*

#### Installation
Clone the repository:
`git clone https://github.com/krsukhorukov/NSFW.git`
Navigate to the project directory:
`cd your_repository`
Install the dependencies:
`pip install -r requirements.txt`
#### Running
To run the API, execute the command:
`uvicorn main:app --reload`
The API will be available at http://127.0.0.1:8000.

#### Usage
###### 1. Upload an image for classification1. Upload an image for classification
Send a POST request to /classify, attaching the image in form data. The image format should be supported (e.g., JPEG, PNG).

*Example usage using curl:*


	> curl -X 'POST'
	'http://127.0.0.1:8000/classify'
	-H 'accept: application/json'
	-H 'Content-Type: multipart/form-data'
	-F 'file=@"/path/to/your/image.jpg"'

###### 2.  Get the result2.  Get the result
The API will return the classification result of the image in a JSON response. Possible result values are: "Censored" or "Not Censored".
Example JSON response:



> 	{
	"result": "Censored"
	}

#### Method Descriptions
###### GET /
Returns a welcome message.

###### POST /classify
Accepts an image for classification. Returns the classification result in a JSON response.

#### Notes
- Image classification is performed using the NSFW Image Detection model, trained based on transformers.

- Temporary image files are saved in the temp directory and deleted after processing.

- If the file format is not an image or errors occur during processing, the API returns appropriate HTTP statuses and error details.



