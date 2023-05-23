insert into yancefoodcali.public.cliente_categoria (nombre_categoria) values 
('Almuerzos'),
('Media tarde'),
('Comidas rápidas'),
('Comidas saludables'),
('Bebidas');

insert into yancefoodcali.public.cliente_producto (nombre,descripcion,precio_unitario,detalle_producto,categoria_id_id) values
('Hamburguesa con papas','Deliciosa hamburguesa con papas a la francesa',18000,'Pan brioche,carne angus 150g, verduras,salsas, papas a la francesa',3),
('Perro caliente (hot dog)','Deliciosa perro caliente con papas a la francesa',15000,'Pan brioche,salchicha americana, ripio de papa,salsas, papas a la francesa',3),
('Salchipapa','Deliciosa sanchipapa',16000,'papa amarilla, salchicha ranchera, salsas y ripio de papa',3),
('Jugo de lulo','Delicioso jugo de lulo en agua',5000,'Fruta fresca',5),
('Jugo de maracuyá','Delicioso jugo de maracuyá en agua',5000,'Fruta fresca',5),
('Coca cola','Delicioso refresco en presentación de 400ml',3500,'Refresco',5),
('Sprite','Delicioso refresco en presentación de 400ml',3500,'Refresco',5),
('Agua con gas','Delicioso refresco en presentación de 400ml',3500,'Refresco',5),
('Agua sin gas','Delicioso refresco en presentación de 400ml',3500,'Refresco',5);

insert into yancefoodcali.public.cliente_inventario (cantidad,producto_id_id) values
(50,1),
(50,2),
(50,3),
(50,4),
(50,5),
(50,6),
(50,7),
(50,8),
(50,9);
