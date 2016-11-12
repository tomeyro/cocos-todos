import cocos
from cocos_todos.layers.LogInLayer import LogInLayer

cocos.director.director.init(width=800, height=480, caption="TODO DESTROYER")
cocos.director.director.run(LogInLayer.create_scene())
