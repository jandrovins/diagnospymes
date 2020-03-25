import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','diagnospymes.settings')
import django
django.setup()
from mm_evaluation.models import *

mps = [None for i in range(11)]
pcs = []
s_pc = []

mps[1] = Macroprocess(name='Manejo del Almacén', number=1)

pcs.append(
    Process(macroprocess_id=mps[1],
    name='Distribución de espacios de almacenamiento',
    description='Hace referencia al control y vigilancia de los espacios que se utilizan dentro de la organización para el almacenamiento de materia prima, insumos y producto terminado.',
    guiding_question='¿Como es la gestión de los espacios que se utilizan para almacenar materia prima y producto terminado?',
    weight=0.25)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se controla el espacio, se almacena en cualquier parte')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se tienen espacios para almacenar pero no se respetan')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tienen espacios designados para almacenar los cuales se planean y se demarcan claramente')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Siempre se siguen unas normas para almacenar en los espacios designados')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se utilizan indicadores para saber el porcentaje de aprovechamiento y uso de los espacios de almacenamiento')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se revisan los indicadores de aprovechamiento y se busca la manera de optimizar los espacios y mejorar los indicadores')
    )

pcs.append(
    Process(macroprocess_id=mps[1],
    name='Transporte materia prima, insumos y producto',
    description='Se refiere a los elementos, guías y métodos utilizados para el traslado de una ubicación a otra de materias primas, insumos, producto en proceso y producto terminado',
    guiding_question='¿Cómo es el transporte de materia prima o producto terminado que será almacenado o que se va a retirar de almacenamiento?',
    weight=0.25)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se le da importancia al transporte de productos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Pocas personas tienen conocimiento de cómo realizar el transporte y suelen transportarse unidades que no son')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Existe documentación sobre cómo debe hacerse el transporte y se planea la cantidad de recursos humanos/máquina que se utilizaran')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='El transporte de cada ítem se encuentra debidamente documentado con su respetiva normativa de seguridad laboral y con sus procedimientos descritos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se calcula la eficiencia del transporte continuamente y las causas de ineficiencia se tienen claramente identificadas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='No existen errores al transportar la materia prima/productos y se atacan todas las fuentes de ineficiencia en equipo')
    )

pcs.append(
    Process(macroprocess_id=mps[1],
    name='Gestión de órdenes del almacén',
    description='Hace referencia al manejo que se les da a las órdenes de producción y por ende a las órdenes para realizar una extracción de materias primas e insumos del almacén de forma ordenada y que mejore el flujo de materiales por la empresa.',
    guiding_question='¿Como es la manera en la que se priorizan, ordenan y muestran las ordenes o solicitudes para retirar materia prima/producto de los lugares de almacenamiento?',
    weight=0.25)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se utilizan métodos para organizar las órdenes del almacén')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se tiene un lugar designado para las ordenes donde no es de fácil acceso y se suelen perder')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tiene un sistema encargado de organizar, priorizar y mostrar las ordenes pendientes')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='La recepción de las ordenes se encuentra estandarizado y se cuenta con técnicas de priorización de las ordenes de acuerdo con las necesidades identificadas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tienen indicadores sobre cantidad de ordenes atendidas, por atender y esperadas que se revisan para realizar la planeación de otros procesos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Las ordenes se completan sin errores y se aplican técnicas de organización y de cultura para evitar perdida de información')
    )

pcs.append(
    Process(macroprocess_id=mps[1],
    name='Picking - Preparación de pedidos',
    description='Hace referencia al proceso de extraer de las posiciones de almacenamiento materiales o producto y que tan simple o complicado se hace ello.',
    guiding_question='¿Se utilizan estrategias para planear y/o realizar la extracción de materia prima o producto terminado de los lugares de almacenamiento?',
    weight=0.25)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se tienen estrategias que faciliten la extracción de materia prima/producto del almacenamiento')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se hace la extracción de los pedidos del almacenamiento por instinto, generando problemas constantes')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se planean las rutas para realizar picking de los diferentes productos, estando documentado para cada uno.')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se utilizan procedimientos y métodos físicos/visuales/auditivos ampliamente documentados que facilitan el picking')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se llevan indicadores de la eficiencia y del porcentaje de éxito del proceso de pickeo, identificando causas de error e ineficiencia')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se busca atacar las causas de error e ineficiencia de pickeo a través rutas más efectivas, reubicación de posiciones de almacenamiento, etc.')
    )
mps[2] = Macroprocess(name='Manejo de Inventarios', number=2)

pcs.append(
    Process(macroprocess_id=mps[2],
    name='Control de niveles de inventarios',
    description='Hace referencia al proceso de revisión y comparación física de los niveles de inventario tanto de materia prima como de producto terminado en los lugares designados para almacenar',
    guiding_question='¿Cómo y con qué estrategias se revisa la cantidad de materia prima o producto terminado que la empresa tiene?',
    weight=0.2)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se revisan y no se sabe la cantidad de materia prima o producto que se tiene')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se revisa los inventarios pero no es una política establecida ni se hace periódicamente')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='La revisión de inventarios es una tarea repetitiva y que se planea para evitar que interrumpa actividades productivas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tienen métodos adecuadamente documentados para la revisión que aseguren tener control sobre la disponibilidad de unidades')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tiene claridad de donde surgen las variaciones entre el valor real y el teórico en las unidades del inventario')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se tienen ayudas visuales (fabrica visual) que facilitan la revisión, se atacan las causas de variación de unidades reales vs teóricas')
    )

pcs.append(
    Process(macroprocess_id=mps[2],
    name='Orden y mantenimiento de inventarios',
    description='El proceso ha referencia a como los encargados de la empresa hacen mantenimiento y aseguran un orden lógico y adecuado a los inventarios para que sea fácil acceder a ellos y sea agradable a la vista al no haber desorden',
    guiding_question='¿Cómo se ordenan los inventarios de modo que sean de fácil acceso y ubicación tanto físicamente como en el sistema de manejo de inventarios que se tenga?',
    weight=0.2)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se realiza un proceso de orden a los inventarios')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se maneja un orden pero se dificulta ubicar ciertos elementos en el inventario')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='El inventario se ordena constantemente y se asegura que todo esté en la ubicación en la que debería')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Existen metodologías documentadas que facilitan el ordenamiento de los inventarios y que aseguran su fácil acceso')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se llevan indicadores de tiempo de búsqueda de inventarios, rotación y cobertura de este')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='El inventario permanece ordenado gracias a un aspecto cultural de organización y a que se está replanteando su orden periódicamente')
    )

pcs.append(
    Process(macroprocess_id=mps[2],
    name='Sistematización de los inventarios',
    description='Se refiere al manejo de los inventarios desde la teoría y desde lo digital: el control de niveles, ubicaciones, calidad, proveedores, clientes y todo lo que se relacione con los inventarios, al ser esta información un reflejo fiel de lo físico.',
    guiding_question='¿Cómo y con que se maneja la información de los inventarios físicos de materia prima y/o producto terminado?',
    weight=0.2)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se tiene ningún sistema que ayude a manejar información de los inventarios')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se llevan registros de información del inventario actual en un sistema básico que suele no ser digital y que es desorganizado')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se cuenta con un sistema documentado que permite almacenar la información básica de los inventarios')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='El sistema para el manejo de inventarios envía alertas sobre las existencias y posee información más detallada del mismo')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Existen indicadores sobre el agotamiento, la cobertura y la rotación del inventario que se calculan con los datos del sistema')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='El sistema ayuda a aumentar la rotación del inventario, la cobertura y a reducir las veces que se generan agotados')
    )

pcs.append(
    Process(macroprocess_id=mps[2],
    name='Reabastecimiento de inventarios',
    description='El proceso contrario al picking, hace referencia de cómo se cargan las posiciones de almacenamiento con materiales y productos. También se conoce como putaway o replenishment a la acción de almacenar inventarios. ',
    guiding_question='¿Cómo se hace ingresan los productos y la materia prima al inventario físico?',
    weight=0.2)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se tiene definido ninguna estrategia para el ingreso de materia prima/producto al inventario')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se realiza el ingreso de productos y materia prima con errores de cantidades y ubicaciones')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se cuentan con estrategias identificadas y documentadas para abastecer de manera rápida el inventario')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Todas las posibles formas de ingresar producto al inventario se tienen identificadas y se tiene estandarizado el proceso')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se utilizan indicadores de eficiencia y productividad para conocer el desempeño del proceso')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se busca aumentar la eficiencia del ingreso de producto al inventario al identificar y atacar las causas de paro y los problemas')
    )

pcs.append(
    Process(macroprocess_id=mps[2],
    name='Control de calidad de los inventarios',
    description='El proceso que consiste en no solamente revisar los inventarios, sino asegurarse que se encuentren con la calidad esperada y que asegure su funcionalidad, que en el caso de productos o materiales perecederos todavía se encuentren hábiles para su aprovechamiento y uso.',
    guiding_question='¿Con que técnicas se realiza la revisión de la calidad de la materia prima y del producto que se encuentra en inventario?',
    weight=0.2)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se revisa la calidad de lo que se encuentra en el inventario')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='El inventario suele dañarse/volverse obsoleto muy seguido por falta de revisión periódica')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tienen planes de inspección de los inventarios que se encuentran documentados')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se utilizan herramientas estadísticas para realizar los muestreos de calidad del inventario')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tienen indicadores de obsolescencia y calidad de los inventarios')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se establecen metas para disminuir las obsolescencias de inventario sin requerir aumentar las revisiones constantes')
    )
mps[3] = Macroprocess(name='Abastecimiento', number=3)

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Certificación a proveedores',
    description='Se refiere al proceso de asegurar que la empresa trabaje con proveedores de confianza y que cumplan con cierto nivel de exigencias a través de revisión de certificaciones o de que la propia empresa se encargue de certificar proveedores bajos unos estándares definidos internamente.',
    guiding_question='¿Cómo hace la empresa para certificar y asegurar la calidad de sus proveedores?',
    weight=0.165)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se certifican y ni se revisan la calidad de los proveedores')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se utilizan algunos proveedores con una certificación pobre')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tienen políticas de trabajar con proveedores con ciertas certificaciones especiales')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tienen estándares propios documentados para certificar o decir que un proveedor es de calidad y está alineado con la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Los estándares que se utiliza para certificar a los proveedores son una mezcla de indicadores internos y certificaciones externas que tienen')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se trabaja únicamente con proveedores certificados y se busca recertificarlos constantemente de acuerdo con normas internacionales')
    )

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Evaluación de proveedores',
    description='El proceso de evaluar en tiempo, costo, calidad y demás factores el desempeño de los proveedores a la hora de trabajar y alinearse con la empresa.',
    guiding_question='¿Cómo y bajo qué criterios se califican y evalúan a los proveedores?',
    weight=0.165)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se evalúa la confiabilidad de los proveedores')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se establecen tiempos límites de entrega de los proveedores que no siempre se cumplen')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se es algo riguroso con el cumplimiento de los proveedores en tiempo, cantidad y calidad')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se evalúa a los proveedores de acuerdo con las prioridades competitivas de la empresa y se les establecen objetivos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='La empresa lleva indicadores claves de cumplimiento en tiempo, calidad, cantidad, costo y eficiencia de servicio')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Los proveedores que no cumplan un mínimo en los indicadores de la empresa entran en un proceso donde se busca su reemplazo')
    )

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Comunicación con proveedores',
    description='Hace referencia al proceso de comunicación por cualquiera que sea el medio con los proveedores que asegure no existan mal entendidos y que finalmente el servicio prestado por ellos sea mejor.',
    guiding_question='¿Cómo y a través de que medios y con qué frecuencia se comunica con los proveedores?',
    weight=0.165)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No existe comunicación con los proveedores')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Comunicación poco asertiva por parte de los proveedores y con limitadas personas tratan.')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tiene un nivel de comunicación aceptable con los proveedores, donde es suficiente para llegar a acuerdos y tratos básico')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tienen procedimientos y se documentan las conversaciones y negociaciones con los proveedores')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tiene una comunicación asertiva con los proveedores, estimando la eficiencia de la comunicación e intentando que sea del 100%')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se tiene una comunicación eficiente con los proveedores que no necesariamente es verbal, ahorrando horas hombre de trabajo')
    )

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Trabajo colaborativo con proveedores',
    description='Se refiere al proceso de compartir y tener cada vez más cerca a los proveedores de la compañía, generar la confianza para compartir datos e información que provoquen una mejora en los niveles de servicio. Abordar más de cerca los conceptos de cadena de suministro al interactuar constantemente para mejorar.',
    guiding_question='¿Como se llevan a cabo los proyectos o actividades conjuntas con los proveedores?',
    weight=0.165)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se trabaja con los proveedores')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Rara vez se realizan reuniones para mejorar conjuntamente y con conversaciones de poco alcance.')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se planea a corto y mediano plazo trabajos colaborativos con los proveedores para hacer más eficiente el abastecimiento')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se establecen objetivos comunes con los proveedores que llevan a trabajar fuertemente en conjunto, planteando actividades de mejora')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='El proveedor cuenta con indicadores de la empresa y la empresa con indicadores del proveedor, para retroalimentarse mutuamente')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Los proveedores son aliados estratégicos de la empresa, se trabaja en conjunto con ellos y se entregan información mutua confidencial')
    )

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Sistema para la gestión de proveedores',
    description='El proceso que refiere al cómo la empresa registra toda la información referente a los proveedores, así como cotizaciones y demás que le permitan tomar decisiones y estar enterado sobre quiénes son sus proveedores. No necesariamente es un sistema digital.',
    guiding_question='¿Cómo se maneja la información de los diferentes proveedores?',
    weight=0.165)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se tiene ningún sistema (no necesariamente digital) para el manejo de información de proveedores')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se llevan registros de información de los proveedores actuales en un sistema básico que suele no ser digital y que es desorganizado')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Existe un sistema digital donde se maneja casi toda la información de los proveedores de manera organizada y de fácil/rápido acceso')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='El sistema digital para manejo de proveedores centraliza toda la información y cuenta con su debida documentación de uso')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='El sistema que maneja los proveedores maneja además los indicadores de cada uno de ellos y envía alertas de incumplimiento de objetivos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='El sistema utilizado para el manejo de proveedores se actualiza y mejora constantemente, realiza tareas operativas de forma autónoma')
    )

pcs.append(
    Process(macroprocess_id=mps[3],
    name='Compras',
    description='Se refiere a todo el proceso que involucra la compra de materiales, servicios y demás, así como la negociación y las estrategias que utiliza la empresa para asegurar comprar cantidad y calidad en los momentos adecuados para evitar futuros desperdicios.',
    guiding_question='¿Cómo es el proceso de compra/adquisición de bienes y servicios?',
    weight=0.165)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se compra cuando o en la cantidad que se necesita realmente')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se compran unidades muy desviadas del pedido realmente necesario y con variaciones de tiempo')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Las compras se monitorean y planean para evitar errores y disminuir los desperdicios por sobre/sub compras')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tiene totalmente documentado como debe hacerse el proceso de compras para cada uno de los insumos de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Existen indicadores de existencia de insumos que indican en qué punto es necesario enviar las órdenes de compra')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Existe conexión con el inventario y producción para que las compras sean cercanas a lo óptimo, no se compra de más y no queda faltando')
    )
mps[4] = Macroprocess(name='Distribución & Servicio al Cliente', number=4)

pcs.append(
    Process(macroprocess_id=mps[4],
    name='Servicio posventa',
    description='Hace referencia al proceso de mantener contacto con los clientes tiempo después de su adquisición, ya sea que existan canales para ello. El tiempo durante el cual se ofrece el servicio y en qué condiciones son elementos claves a considerar del proceso.',
    guiding_question='¿Se hace y como contacto con los clientes una vez adquieren los productos para asegurar el mejor servicio?',
    weight=0.2)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se tiene contacto con los clientes una vez ofrecido el servicio')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se tiene contacto con algunos clientes pero no es claro ni constante la comunicación')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se ofrece un soporte sencillo (documentado) posventa a los clientes para asegurar su satisfacción con el producto/servicio')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Existe un canal y/o un personal dedicado en mantenerse en contacto con cliente estratégicos para asegurar la satisfacción de ellos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tienen indicadores y herramientas que permiten conocer la satisfacción del cliente tanto frente al servicio como frente al producto')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='La empresa busca cada vez ofrecer un mejor servicio y una mejor cobertura al cliente, estar enterado de nuevos requerimientos')
    )

pcs.append(
    Process(macroprocess_id=mps[4],
    name='Rastreo de pedidos enviados',
    description='El proceso de tener vigilancia y control sobre los productos que salen de la empresa. Los productos saliente no solo se limitan a la distribución de pedidos, sino también a devoluciones y demás.',
    guiding_question='¿Se lleva y como una trazabilidad de todo producto propiedad de la empresa que se encuentra siendo transportada?',
    weight=0.2)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se realiza trazabilidad de los pedidos en transito')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se tiene información de pocos productos y solo durante un corto tiempo de su ubicación, la cual no es siempre precisa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Los pedidos se monitorean cada cierto tiempo gracias a unos puntos de control donde se informa acerca del estado de ellos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tiene información constante del estado de los pedidos y se sigue un protocolo establecido para llevar el control adecuado')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Existen indicadores de precisión, y de probabilidad de éxito y entrega perfecta de acuerdo con el rastreo de los pedidos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se tiene información de los pedidos en tiempo real, se están revisando los estados y la probabilidad de éxito de la operación')
    )

pcs.append(
    Process(macroprocess_id=mps[4],
    name='Garantía de la satisfacción cliente',
    description='Hace referencia a los esfuerzos ejecutados por la empresa para asegurar que el cliente reciba un producto con la calidad esperada.',
    guiding_question='¿Se ofrece y de que tipo garantías a los clientes ante producto con defectos o por no conformidad ante el mismo?',
    weight=0.2)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se ofrece ningún tipo de garantía a los clientes')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se ofrecen garantías a criterio del momento en el que ocurre, no encontrándose documentado las condiciones')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Existen estándares básicos bajo los cuales se ofrecen garantías, y solamente se ofrecen bajo dichas políticas empresariales')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='La empresa tiene las condiciones bajo las cuales ofrece garantías claramente definidas, documentadas e informadas a los clientes')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='La empresa conoce gracias a un Pareto bajo que casos los clientes solicitan garantía y trabaja para reducir dichas incidencias')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='La empresa se asegura de cumplir gran parte de las solicitudes de garantía que se encuentren dentro de la documentación de esta')
    )

pcs.append(
    Process(macroprocess_id=mps[4],
    name='Distribución de pedidos',
    description='El proceso de entrega y distribución de los pedidos ya sea a través de una flota propia, tercerizada o mixta a los distintos clientes con los que cuente la organización.',
    guiding_question='¿Cómo se realizan las entregas de productos a los clientes?',
    weight=0.2)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se ofrece ningún servicio de entrega al clientes, ni siquiera tercerizado')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Existe una persona o entidad encargada de la distribución, realizándola por experiencia propia, sin planear rutas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Diariamente se planean y documentan las rutas que se van a utilizar para realizar las entregas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='La distribución se encuentra totalmente estandarizada gracias a procedimientos y rutas definidas y estudiadas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se mide la eficiencia del proceso ya estandarizado de distribución y se identifican causas que afecten dicha eficiencia')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se realizan ruteos y procesos de optimización de rutas y tiempos para asegurar un nivel de servicio alto en el transporte')
    )

pcs.append(
    Process(macroprocess_id=mps[4],
    name='Devoluciones de producto',
    description='Se refiere a la logística inversa, es decir la manera en la que la empresa recibe y procesa las devoluciones por calidad de su producto.',
    guiding_question='¿Cómo se manejan los pedidos que se devuelven por tema de calidad o de conformidad?',
    weight=0.2)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se aceptan devoluciones de producto con defectos de calidad o por inconformidades')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se aceptan devoluciones en algunos casos de acuerdo con el criterio del encargado del momento.')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tienen definidas y documentadas algunas situaciones o casos bajo los cuales se aceptan devoluciones, y su respectiva acción posterior')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tiene plenamente identificadas y documentadas las políticas de devoluciones, asimismo son de conocimiento del cliente')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tienen paretos para identificar numéricamente la causas más frecuentes de devoluciones para trabajar sobre ellas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se trabaja de forma transversal en toda la empresa para asegurar la calidad del producto y disminuir las devoluciones')
    )
mps[5] = Macroprocess(name='Planeación Estratégica', number=5)

pcs.append(
    Process(macroprocess_id=mps[5],
    name='Planeación de demanda - Pronósticos',
    description='Hace referencia a las técnicas que utiliza la empresa para prever las ventas de acuerdo con datos históricos pasados, que ayuden a determinar comportamientos futuros.',
    guiding_question='¿Cómo se realizan los pronósticos de ventas?',
    weight=0.25)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se utiliza ninguna herramienta o método para realizar pronósticos de venta')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se realizan pronósticos a corto plazo a experiencia propia y sin apoyo matemático, sin evaluar el resultado de los pronósticos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se utiliza un modelo de pronósticos que funciona para la empresa aparentemente pero no se evalúa su precisión')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='La empresa utiliza una herramienta que le permite elaborar diferentes modelos matemáticos de pronósticos y comprarlos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se llevan indicadores de exactitud/precisión de los pronósticos, evaluando diferentes modelos de pronósticos para ver cual se adapta mejor')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se tiene un equipo y reuniones de planeación de venta y operaciones donde se estudian los pronósticos y se busca mejorar la medición')
    )

pcs.append(
    Process(macroprocess_id=mps[5],
    name='Planeación oferta - Plan de producción',
    description='Se refiere al proceso de planear los recursos necesarios para ejecutar la producción a corto y mediano plazo de acuerdo con proyecciones realizadas. Involucra desde capacidad del personal, de la maquinaria, así como los costos asociados a ello.',
    guiding_question='¿Cómo se realizan los planes de producción de la empresa?',
    weight=0.25)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se realizan planes de producción a mediano/largo plazo')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se planean aspectos muy generales para la producción y no se integra la información de toda la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se realizan planes de producción teniendo en cuenta información veraz de gran parte de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Existe una herramienta que permite en los planes de oferta/producción contar con información integrada de todas las áreas de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se llevan indicadores sobre la desviación de los planes de producción versus la real, utilizándola para alimentar la herramienta usada')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se tiene un equipo y reuniones de planeación de venta y operaciones donde se estudian los planes agregados y se buscan mejorar')
    )

pcs.append(
    Process(macroprocess_id=mps[5],
    name='Estimaciones de crecimiento',
    description='Hace referencia a planear y establecer una meta del crecimiento de la empresa, plantear estrategias y actividades del día a día que apunten a esa meta. El crecimiento como el buscar más que el solo sostenimiento económico.',
    guiding_question='¿Cómo se planea el crecimiento económico y productivo de la empresa?',
    weight=0.25)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se tiene ningún plan o proyección a futuro del crecimiento empresarial')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se fijan puntos donde se desea estar a futuro pero no se establecen acciones que apunten fuertemente a ello')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se planean acciones que apoyen y apunten al crecimiento físico y económico de algunas áreas específicas de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se establecen objetivos de crecimiento económico y financiero que se encuentren alineados con las políticas y estrategias de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tienen indicadores de lo que se espera crecer, lo crecido y el cumplimiento de tareas que apunten al cumplimiento de objetivos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Existen proyecciones de crecimiento y se hacen simulaciones para entender las necesidades futuras y plantear los nuevos retos emergentes')
    )

pcs.append(
    Process(macroprocess_id=mps[5],
    name='Planeación de expansión física',
    description='Se refiere a la gestión actual de la infraestructura física de la empresa y las proyecciones que tiene en cuanto a su potencial utilización en el futuro para generar utilidades. Hace referencia también a plantear la necesidad de capacidad adicional de acuerdo con crecimiento de demanda esperados.',
    guiding_question='¿Cómo se planea la expansión de los espacios físicos a futuro?',
    weight=0.25)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se planea la expansión física de la empresa.')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se dejan espacios aleatorios disponibles, ya sea porque sobran o por si se llegaran a necesitar')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='La empresa cuenta con espacio suficiente para las operaciones actuales y cuenta con una pequeña reserva de espacio para expandirse')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='La empresa cuenta con simulaciones/escenarios de crecimiento que le permiten determinar el espacio físico que requiere en el futuro')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tiene claridad del porcentaje de crecimiento físico esperado a mediano y largo plazo, así como la identificación de la variación de este')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se tienen estrategias totalmente definidas para la expansión física de la empresa, conociendo la necesidad de espacio, económica, etc.')
    )
mps[6] = Macroprocess(name='Manejo del Recurso Humano', number=6)

pcs.append(
    Process(macroprocess_id=mps[6],
    name='Motivación y desempeño de empleados',
    description='Hace referencia al control sobre la motivación y el desempeño actual de los empleados en los lugares y puestos donde se encuentran trabajando ',
    guiding_question='¿Cómo se mide la motivación que tienen los diferentes empleados y colaboradores de la empresa?',
    weight=0.165)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se conoce la motivación de los empleados y/o colaboradores')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se conoce medianamente la motivación de los empleados por conversaciones informales.')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se hacen encuestas y/o entrevistas serias planeadas para conocer la motivación de los empleados')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tiene como objetivo fundamental que la mayoría de los empleados se sienta a gusto con su trabajo, haciéndolos participes de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se cuenta con indicadores e historia de la medición de la motivación de los empleados y estadísticos significativos para su entendimiento')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se busca que los empleados se encuentren motivados, se les hace participes de las decisiones y se les brindan incentivos varios')
    )

pcs.append(
    Process(macroprocess_id=mps[6],
    name='Capacitaciones al personal',
    description='Se refiere al proceso de capacitar y mantener actualizados en conocimientos del área al personal para asegurar que la empresa sea competitiva desde su recurso humano.',
    guiding_question='¿Cómo y cada cuanto se realizan capacitaciones/talleres/cursos para mantener actualizados a los empleados?',
    weight=0.165)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se capacitan ni certifican los empleados')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se realizan algunas charlas internas dirigidas por los mismos empleados, que no son constantes en el tiempo')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se planean charlas y capacitaciones que aporten en la formación profesional de los empleados de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Además de planear charlas que aporten al crecimiento profesional, se comparte conocimiento entre los mismos empleados de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se manejan indicadores de la cantidad y calidad de las capacitaciones en términos de su impacto en las tareas diarias de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='La organización busca cada vez brindar más capacitaciones con expertos que aumenten los conocimientos prácticos de los empleados')
    )

pcs.append(
    Process(macroprocess_id=mps[6],
    name='Control niveles de estudio del personal',
    description='El proceso se refiere a la vigilancia que hace la empresa sobre las aptitudes y el nivel educativo con el que cuenta cada uno de los empleados para asignarle tareas correspondientes con sus verdaderas capacidades.',
    guiding_question='¿Cómo se controla que los empleados tengan el nivel educativo adecuado para el puesto que desempeñan?',
    weight=0.165)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se conoce el nivel educativo del personal para ser asignado a tareas acordes')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Las personas suelen encontrarse sin las aptitudes para realizar sus labores')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='La mayoría de las personas cuentan con niveles mínimos de estudio/capacitación para desarrollar las tareas que tienen asignadas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Todas las personas se encuentran en puestos de trabajo acorde a su nivel educativo de forma que puedan aportar a la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tienen indicadores que muestran los niveles de aptitud de cada uno de los empleados para cada una de las tareas que podría realizar')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='La empresa busca desarrollar a sus empleados y los apoya en tiempo y/o dinero para que estudien carreras universitarias o cursos')
    )

pcs.append(
    Process(macroprocess_id=mps[6],
    name='Adecuación lugares de trabajo',
    description='El proceso de asegurar que los lugares de trabajo sean adecuados para las tareas que allí se realizan en temas de orden, limpieza, disponibilidad y ergonomía. ',
    guiding_question='¿Cómo se tienen organizados los diferentes puestos de trabajo de los empleados?',
    weight=0.165)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se cuenta con puestos de trabajo limpios y ordenados')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Los empleados tienen puestos de trabajo cómodos pero desordenados u ocupados con elementos que no tienen que ver con sus labores')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Los puestos de trabajo se mantienen limpios y mantienen bajo constantemente revisión por el personal encargado de la limpieza')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Existen estándares y procedimientos de cómo deben mantener y como debe realizarse la limpieza de los diferentes puestos de trabajo')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se utilizan indicadores para evaluar la adecuación, limpieza y orden de los puestos, así como el cumplimiento en el aseo de ellos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se utilizan herramientas de mejora continua en los puestos de trabajo que incentiven el orden y la limpieza como las 5S y los Poka Yoke')
    )
mps[7] = Macroprocess(name='Ventas', number=7)

pcs.append(
    Process(macroprocess_id=mps[7],
    name='Estrategias y nivel de venta',
    description='Hace referencia a todas las estrategias de mercadeo utilizadas para vender y su respectivo impacto generado en ventas reales.',
    guiding_question='¿Cómo y cuánto se vende respecto a lo que se esperaría vender?',
    weight=0.5)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se tienen estrategias de venta, las ventas son bajas.')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se depende de las estrategias individuales para el aumento de ventas, que no se encuentran sustentadas en números o planeación')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Existen estrategias documentadas y probadas que ayudan a mantener incluso aumentar el nivel de ventas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se establecen objetivos de ventas y se siguen unas metodologías estandarizadas para alcanzar dichos niveles de venta')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Existen indicadores para calificar el impacto de las estrategias planeadas de ventas utilizadas versus la ventas alcanzadas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se investigan e implementan estrategias nuevas e innovadoras que aumenten las ventas, evaluándose continuamente')
    )

pcs.append(
    Process(macroprocess_id=mps[7],
    name='Exportaciones',
    description='El proceso correspondiente a internacionalización y abarcar nuevos mercados con los productos ofrecidos, así como el proceso logístico que lleva a ello como los contactos, las investigaciones y el transporte.',
    guiding_question='¿Cómo se exporta?',
    weight=0.5)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se realizan exportaciones')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se realizan o se planean algunas exportaciones que no generan mucha utilidad para la empresa respecto al esfuerzo que requiere')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se realizan un número considerable de exportaciones por periodo de tiempo, que se planean con tiempo con tiempo suficiente')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Las exportaciones son un proceso estandarizado y que cuenta con procedimientos actividades documentadas que facilitan dicho proceso')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se llevan indicadores sobre los niveles actuales de exportación, así como la capacidad exportadora a diferentes regiones internacionales')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Parte importante de las ventas de la empresa son las exportaciones, teniendo un sistema y aliados internacionales que lo facilitan')
    )
mps[8] = Macroprocess(name='Producción', number=8)

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Balanceo de líneas de producción',
    description='Hace referencia al proceso de identificar cuellos de botella en el proceso productivo y su correcto balanceo de cargas para equilibrar el sistema.',
    guiding_question='¿Como se asignan las tareas operativas para que sean igualmente justas?',
    weight=0.125)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se nivelan cargas generando cuellos de botella grandes')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se detectan posibles cuellos de botella en la producción que no se atacan directamente')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Constantemente se establecen acciones pequeñas que ayuden a eliminar los cuellos de botella detectados en el proceso')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se utilizan modelos, metodologías y/o heurísticos que ayuden a equilibrar cargas de trabajo en las operaciones de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tienen indicadores de ocupación, utilización y eficiencia en cada una de las tareas operativas, facilitando identificar el cuello de botella')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se está constantemente revisando la capacidad de los procesos y buscando liberar y balancear las cargas para eliminar cuellos de botella')
    )

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Flexibilidad del proceso productivo',
    description='Se refiere a los esfuerzo realizados por la empresa para cumplir a nivel productivo de manera ágil con los cambios en las necesidades de los clientes y poder entregar a ellos lo que requieren.',
    guiding_question='¿Cómo se les facilita flexibilidad a los procesos, ante las necesidades del mercado?',
    weight=0.125)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se permiten modificaciones de clientes al producto ofrecido')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='El cambio de referencia tarda mucho tiempo al no existen dispositivos que ayuden a ello, dificultando la personalización del producto')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se ofrecen pequeñas personalizaciones a los productos, teniendo además técnicas que facilitan los cambios de referencia')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tienen estrategias definidas y dispositivos que permiten un mayor nivel de personalización en los productos sin dificultad alguna')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Los clientes hacen parte importante del proceso de diseño del producto, se llevan indicadores de la eficiencia en los cambios de referencia')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Cada vez el cliente está más cerca del proceso y se tienen múltiples dispositivos y estrategias como SMED para los cambios de referencia')
    )

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Control de la producción',
    description='Se refiere al nivel de control que tiene el encargado de la producción sobre ella, que le permite tomar decisiones clave como el tipo, cantidad, calidad, y demás parámetros de la producción de forma rápida y efectiva.',
    guiding_question='¿Cómo se controla la cantidad y el tipo de producto que se producen en determinados momentos?',
    weight=0.125)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se controla generalmente la cantidad de producción que sale.')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se tienen datos de la producción solamente al final del día, algunas veces no es un dato preciso')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tienen datos reales de producción periódicamente sobre cantidad y tipo de producto, concordando con los planes de producción')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tienen dispositivos, alertas, sensores o estrategias que controlan la producción y cumplir la meta o por el contrario evitar sobre producir')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='La producción maneja indicadores de productividad total y eficiencia de cada uno de los procesos, que permite plantear puntos débiles')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se tiene control en todo momento del proceso productivo, conociendo la producción y siendo capaz de tomar decisiones en tiempo real')
    )

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Comunicación de información',
    description='El proceso corresponde al manejo y transmisión de información a nivel de producción que permite a la empresa estar en la misma página sobre todo a nivel operativo con los niveles estratégico y táctico, evitando errores por desalineamiento.',
    guiding_question='¿Cómo se maneja y comunica la información de producción a todos los relacionados?',
    weight=0.125)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se transmite la información del proceso productivo a quienes debería')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='La información que se maneja es muy limitada y no llega en el momento que realmente se necesita')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se manejan canales informales de comunicación, voz a voz buscando difundir la información a los interesados')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Existen canales visuales y/o auditivos que permiten comunicar la información de manera eficaz')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se evalúa el impacto, el alcance y la pertinencia de los canales utilizados para comunicar la información')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se buscan canales de transmisión de información cada vez de mayor alcance y eficiencia, llegando más rápido a los empleados')
    )

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Estandarización de procesos',
    description='Corresponde a los esfuerzo y estrategias utilizados por la empresa para facilitar y agilizar los procesos productivos al adicionalmente simplificar su oferta de producto.',
    guiding_question='¿Cómo se busca estandarizar/facilitar los procesos productivos?',
    weight=0.125)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se hacen esfuerzos por estandarizar procesos y/o tareas.')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se tienen estandarizadas (no formalmente) algunas tareas muy operativas del proceso productivo')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Cada proceso operativo/administrativo cuenta con las herramientas necesarias para trabajar cerca')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Todos los procesos se encuentran plenamente documentados bajo la gestión por procesos, de forma que sea fácil delegar tareas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tienen indicadores sobre la cantidad de procesos estandarizados y el porcentaje de estandarización con el que cuentan')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Todos los procesos se encuentran en búsqueda de una estandarización y se evalúa dicha estandarización para hacer el proceso más eficiente')
    )

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Costeo de producción',
    description='Se refiere al proceso de identificar los diferentes costos y gastos que involucra la transformación de materiales: mano de obra, compras e indirectos, y la gestión para disminuirlos sin afectar el producto.',
    guiding_question='¿Cómo se calculan los costos y gastos relativos al proceso productivo?',
    weight=0.125)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se calculan los costos/gastos generados por el área de producción')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se cargan únicamente los costos que son directos al producto o se cargan los costos de manera arbitraria')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tienen en cuenta todos los costos y se busca la manera de distribuirlos equitativamente entre la producción')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Los costos indirectos se realizan basados en actividades, se revisan constantemente para ser actualizados en junto con los costos directos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tiene identificado los costos que agregan y no valor finalmente al producto, además de cálculos del EBITDA y sus formas de mejorar')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se está en constante disminución y eliminación de costos, costea con técnicas como ABC u otras que dan una panorama real de la empresa')
    )

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Control de calidad producción',
    description='Hace referencia a las técnicas utilizadas por la empresa para asegurar la calidad del producto desde la misma producción y evitar que posibles errores que se generen se sigan generando y produciendo.',
    guiding_question='¿Con que técnicas se realiza la revisión de la calidad de los productos que se van produciendo o se produjeron?',
    weight=0.125)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se revisa la calidad de la producción que se hace')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Al final del proceso productivo se acepta o rechaza uno a uno la producción de acuerdo con un criterio individual')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tienen planes de inspección de calidad aleatorios para algunos lotes de producción')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tienen documentados las causas de rechazo de producto y cada inspección planeada se rige bajo dichas causas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se utilizan nociones de herramientas de muestreo estadístico (ej. Tablas militares) para el control de calidad de la producción')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se utilizan técnicas como el lean six sigma y otras de mejora continua para asegurar la calidad de la producción')
    )

pcs.append(
    Process(macroprocess_id=mps[8],
    name='Reprocesamiento',
    description='El proceso hace referencia a todos los productos que por motivos de calidad no pudieron salir a la venta o que salieron y fueron retornados por los mismos temas de calidad, que se vuelven a procesar para que no se conviertan en desechos totalmente y poder generar algo de rentabilidad de ellos.',
    guiding_question='¿Cómo se manejan los productos defectuosos que deben ser reprocesados?',
    weight=0.125)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se realizan reprocesos, se descartan')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Los reprocesos además de disminuir casi a cero las utilidades, son complicados y entorpecen el proceso normal')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tiene claridad en cómo hacer los reprocesamientos y se cuenta con personal en capacidad de realizarlos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Existen procedimientos que se siguen al pie de la letra para minimizar las pérdidas durante los reprocesos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Existen paretos donde se tienen identificadas y cuantificadas las principales causas de reproceso y se establecen acciones para mejorar')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se trabaja de forma transversal en toda la empresa para asegurar la calidad del producto y disminuir los reprocesos necesarios')
    )
mps[9] = Macroprocess(name='Organizacional', number=9)

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Colaboración interempresarial',
    description='Se refiere como la empresa se relaciona, trabaja, asocia y alinea con otras empresas que le permita utilizarlas como apalancamiento para la mejora de su competitividad. El apalancamiento para la competitividad se hace mutuamente.',
    guiding_question='¿Cómo es la colaboración y la ayuda con y por parte de otras empresas?',
    weight=0.142)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No existe colaboración ni alianzas con otras empresas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se tiene una comunicación limitada con unas pocas empresas cercanas para pequeñas ayudas mutuas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='La empresa tiene alianzas con empresas del mismo sector con las cuales puede apoyarse en actividades de tipo clúster')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='La empresa se apoya estratégicamente de otras empresas, se realizan actividades en conjunto para aumentar la productividad')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Entre las empresas existen indicadores de productividad para calificarse entre ellas y aportar al mejoramiento conjunto de los procesos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='La empresa hace parte de grandes sociedades con otras compañías donde se evalúan y colaboran mutuamente, tipo clúster')
    )

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Financiación',
    description='El proceso hace referencia a la búsqueda de la empresa por financiar las ideas que se tengan en pro de la mejora empresarial, tanto con entidades públicas y privadas. Asimismo se refiere a todo el proceso de estudio que se requiere previo a solicitar una financiación.',
    guiding_question='¿Cómo busca la empresa financiar los proyectos y las ideas que tiene?',
    weight=0.142)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se busca ningún tipo de financiamiento o apoyo económico')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='La empresa tiene conocimiento de algunos medios para financiarse pero no ha tenido oportunidad de utilizarlos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='La empresa reconoce las necesidad de financiarse para desarrollar los planes de crecimiento, buscando realizarlo')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='La empresa ha contado con proyectos de financiación, reconociendo sus ventajas y gracias a ello ha podido crecer')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='La empresa tiene identificado el porcentaje de sus proyectos que deben ser financiados para cumplir con los planes estratégicos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='La empresa siempre revisa las necesidades de financiación versus las opciones, encontrando la mejor manera de financiarse')
    )

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Apropiamiento tecnológico e Industria 4.0',
    description='Hace referencia a la apropiación y tendencia al uso e incorporación de infraestructura tecnológica y referente a la cuarta revolución industrial en los procesos productivos como una ventaja competitiva que ayude al marginamiento de la empresa.',
    guiding_question='¿Cómo es la gestión de la tecnología y la aproximación a industria 4.0 en la empresa?',
    weight=0.142)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se tiene y se desconoce cualquier acercamiento a Industria 4.0')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se utilizan equipos de cómputo e internet para almacenar información sobre la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se utilizan sistemas, software y la nube para realizar diferentes actividades de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Todos los sistemas y la información de la empresa se encuentra digitalizada y documentada, siendo de fácil acceso')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='La empresa basa gran parte de sus procesos y tareas operativa y administrativas en el uso de TICs que aumentan la productividad')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='La empresa cuenta con servicios interconectados, alojamiento en la nube y disponibilidad en tiempo real de información')
    )

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Innovación',
    description='El proceso corresponde a todas las acciones novedosas y diferentes que nacen como ideas desde el personal de la empresa y que se terminan ejecutando para finalmente generar algún tipo de beneficio.',
    guiding_question='¿Cómo se gestionan las ideas innovadoras para la mejora de la empresa?',
    weight=0.142)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se realiza gestión alguna para innovar los procesos de la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se premian las ideas para innovar mas no se tienen equipos y personas encargadas de ello')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tienen personas con tareas secundarias de buscar maneras de innovar el proceso y documentar las ideas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se tienen procedimientos donde se describen las actividades para el desarrollo de ideas innovadoras propuestas por los empleados')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se evalúa el impacto y la mejora en la eficiencia gracias a las diferentes innovaciones, se tiene un equipo exclusivo a cargo de ellas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se utilizan técnicas modernas de producción y administración, utiliza software especializado y se premian las mejoras en eficiencia')
    )

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Distribución de tiempo',
    description='Hace referencia a la planeación del tiempo tanto de individuos como de colectivos para cumplir con las actividades diarias de la empresa.',
    guiding_question='¿Cómo se distribuye el tiempo para cumplir con las necesidades del día a día?',
    weight=0.142)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se distribuye el tiempo adecuadamente para cumplir con las tareas diarias')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Las jornadas de trabajo suelen alargarse sin planearlo y no se sabe con certeza cuanto más suelen alargarse')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se planean horas extras anticipadamente en caso de ser necesaria para cumplir con los compromisos productivos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se cuenta con personal y capacidad suficientes para aprovechar al máximo la jornada laboral, minimizando la cantidad de horas extras')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Existen indicadores de la ocupación de todos los empleados, teniendo estadísticas sobre la necesidad de tiempo extra')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se está siempre en búsqueda de MUDAS, ineficiencias o tiempos ociosos para atacarlas y maximizar el aprovechamiento de la jornada')
    )

pcs.append(
    Process(macroprocess_id=mps[9],
    name='Cultura organizacional',
    description='Se refiere al proceso de idear estrategias que aseguren que el personal se apropie de la empresa para asegurar que cuiden y apoyen el crecimiento de la empresa, así como el mantener el recurso humano dentro de la misma.',
    guiding_question='¿Cómo es la cultura y el sentido de pertenencia de los empleados de la empresa?',
    weight=0.142)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se tiene una cultura y los empleados no tienen sentido de pertenencia')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='El personal procura mantener su área de trabajo apta para laborar, mas no es un trabajo conjunto')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='El orden es una tarea repetitiva e importante en todos los empleados como conjunto, además se brindan pequeños incentivos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='La empresa realiza campañas internas para promover la cultura, el orden y el sentido de pertenencia de los empleados')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se llevan indicadores del impacto de las campañas de promoción cultural, así como estadísticas de aportes de los empleados a la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Es evidente como los empleados sienten como suya la empresa, participan activamente y buscan hacerla cada vez más grande y competitiva')
    )

pcs.append(
    Process(macroprocess_id=mps[9],
    name='I+D de productos y servicios nuevos',
    description='El proceso que corresponde con la investigación y generación de nuevas ideas de productos y servicios, así como su posterior desarrollo y lanzamiento, que aseguren a la empresa una diversificación del catálogo de productos y una permanencia en el mercado.',
    guiding_question='¿Cómo es el proceso de investigación y desarrollo de nuevos productos?',
    weight=0.142)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se desarrollan productos nuevos que requieran investigación')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Los nuevos desarrollos se basan de las investigaciones o desarrollos de otras empresas o de personas externas a la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='La empresa planea sus propios desarrollos de producto y busca ayudas externas para ello')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Existen metodologías y procedimientos que le permiten a la empresa realizar sus propias investigaciones y desarrollos internamente')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='La empresa maneja estadísticas sobre los desarrollos propios y su recepción en el mercado, así como proyecciones de futuros desarrollos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Se cuentan con una área de investigación y desarrollo propiamente que está en la búsqueda constantes de nuevas oportunidades')
    )
mps[10] = Macroprocess(name='Externas', number=10)

pcs.append(
    Process(macroprocess_id=mps[10],
    name='Respuesta a políticas gubernamentales',
    description='El proceso se refiere a como la empresa anticipa y se prepara para responder a políticas establecidas por los gobiernos locales. Adicionalmente los planes de respaldo con los que cuenta a situaciones que puedan ser extremas y que pongan a prueba la resiliencia empresarial.',
    guiding_question='¿Cuál es la reacción de la empresa ante políticas de gobierno que la afectan?',
    weight=0.33)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se toman acciones como respuesta a políticas de gobierno que afecten la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='Se conocen algunos de los efectos de las políticas gubernamentales sobre la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='Se tienen acciones documentadas que ayuden a contrarrestar las políticas que afectan a la empresa')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se lleva control constante de las políticas gubernamentales actuales, planteando las respectivas acciones para contrarrestar los efectos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se lleva en indicadores propios de la empresa el efecto de las políticas gubernamentales sobre ella, y las probabilidades de afectación')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='La empresa no se ve afectada ante las políticas gubernamentales gracias a los planes de contingencia y la trazabilidad de políticas')
    )

pcs.append(
    Process(macroprocess_id=mps[10],
    name='Estabilidad económica de la empresa',
    description='Se refiere al proceso de asegurar que a pesar de las inestabilidades geopolíticas y económicas de los gobiernos locales, la empresa cuente con la solidez para sobrevivir y salir delante a pesar de ello. Igualmente corresponde a la búsqueda de independencia empresarial y económica.',
    guiding_question='¿Cuál es el nivel de estabilidad e independencia económica que tiene la empresa?',
    weight=0.33)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se tiene estabilidad ni independencia económica')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='La empresa suele sufrir por los cambios económicos y no se realizan acciones preventivas para dichos cambios')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='La empresa monitorea los principales indicadores económicos y evalúa su impacto en el funcionamiento de esta')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Se cuenta con planes de respaldo ante inestabilidades económicas como recesiones, caída de acciones, variación del dólar, etc.')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='Se tiene identificadas que situaciones económicas particulares afectan la empresa y como se pueden prevenir algunos efectos negativos')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='La empresa se adelanta y utiliza modelos matemáticos y económicos para detectar futuras variaciones y prepararse para ellas')
    )

pcs.append(
    Process(macroprocess_id=mps[10],
    name='Participación en iniciativas públicas',
    description='El proceso que corresponde con la participación en iniciativas y programas públicos que se desarrollan localmente para apoyar a la micro y pequeña empresa en su desarrollo. Corresponde también a la financiación, la excepción de impuestos o cualquier otra ayuda adicional dada por el gobierno para aportar al crecimiento de las pequeñas empresas en el país.',
    guiding_question='¿Cuál es el nivel de participación de la empresa en iniciativas y programas públicos para la mejora de la competitividad de empresas?',
    weight=0.33)
    )
#SpecificPractices for ^^ process:

s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=0,
    description='No se participa ni se ha participado en programas públicos para incentivar la competitividad de empresas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=1,
    description='La empresa conoce de algunas pocas iniciativas públicas y ha intentado participar en algunas de ellas con éxito variable')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=2,
    description='La empresa es curiosa y planea con tiempo la participación en iniciativas públicas que le ayuden a la mejora de la competitividad')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=3,
    description='Es frecuente que la empresa participe en sociedades e iniciativas públicas, además hace parte de grupos de apoyo de las grandes empresas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=4,
    description='La empresa cuenta con una base de datos de iniciativas y convocatorias, identificando la conveniencia/alcance de cada una de ellas')
    )
s_pc.append(
    SpecificPractice(process_id=pcs[-1],
    score=5,
    description='Participación constante y activa de iniciativas, ferias y eventos importantes tanto nacionales como internacionales"')
    )


for mp in mps[1:]:
    mp.save()

for p in pcs[:]:
    p.save()

for sp in s_pc[:]:
    sp.save()