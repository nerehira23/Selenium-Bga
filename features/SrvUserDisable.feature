Feature: Acceso


  Scenario: Usuario no se encuentra habilitado
  Given El usuario ingresa a la página web de Gananet
  When El usuario selecciono el tipo de usuario Alias
  Then E ingreso el usuario ALIAS y hago clic en verificar
  Then Obtiene un mensaje restrictivo