Bienvenido a ModelChat

Empieza a usar ModelChat
ModelChat es una libreria gratuita para implementar modelos de lenguaje alojados en Huggingface de forma mas simple y menos compleja 
La tarea principal de ModelChat es su uso en la creacion de chatbots o bots Conversacionales con python
ModelChat tambien puede implementarce en bots como Telegram y Discord

instala ModelChat:
```shell
pip3 install ModelChat
```

Uso de ModelChat:
```python
from ModelChat import simulate_conversation


chatbot=simulate_conversation(
    model_name='OpenAssistant/oasst-sft-1-pythia-12b',
    token='XXXXX',
    prompt='Simulate a Conversation With an AI her name is Mia (Artificial Intelligence Model) she is smart and friendly she likes to talk a lot, she speaks mainly in Spanish',
    user_intent='Mensaje que mandas al modelo,
    max_tokens=1024,
  )

print('Bot:', chatbot)
```

Recuerda que en el apartado de Model Name='Puedes poner Cualquier modelo alojado en Huggingface', token='', es el valor del token que generes en huggingface recuerda registrarte antes, prompt='', es para darle un rol al modelo de lenguaje, user_intent='' En este apartado va tu mensaje que respondera el modelo,
max_tokens='' numero maximo de tokens que usara el modelo el limite es de 1024