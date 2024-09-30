
class Seguridad:

    __ADMIN = 1462438140
    __usuariosPermitidos = [0]


    def __init__(self):
        self.__usuariosPermitidos[0] = self.__ADMIN

    def verificar_usuario(self, user_id:int):
        if user_id in self.__usuariosPermitidos:
            return True
        else:
            return False

    def permitir_usuario(self, user_id:int):
        
        self.__usuariosPermitidos.append(user_id)

    def ver_admin(self):
        return self.__ADMIN
    def borrar_usuario(self, user_id):
        if(self.verificar_usuario(user_id=user_id) == True):
            self.__usuariosPermitidos.remove(user_id)
        else:
            pass
    def ver_usuarios(self):
        return self.__usuariosPermitidos


