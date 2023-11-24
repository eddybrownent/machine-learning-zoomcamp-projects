FROM agrigorev/zoomcamp-bees-wasps:v2

RUN pip install keras-image-helper
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl


COPY Homework_9.py .
ENV MODEL_NAME=bees-wasps-v2.tflite

CMD [ "Homework_9.lambda_handler" ]
