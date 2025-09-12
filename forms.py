from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Título de la Publicación", validators=[DataRequired(), Length(min=5, max=250)])
    subtitle = StringField("Subtítulo", validators=[DataRequired(), Length(min=5, max=250)])
    img_url = StringField("URL de la Imagen", validators=[DataRequired(), URL()],
                          render_kw={"placeholder": "https://ejemplo.com/imagen.jpg"})

    # Categoría para organizar mejor el contenido
    category = SelectField("Categoría",
                           choices=[
                               ('', 'Selecciona una categoría'),
                               ('noticias', 'Noticias de IA'),
                               ('investigacion', 'Investigación'),
                               ('herramientas', 'Herramientas y Tecnología'),
                               ('anestesiologia', 'Anestesiología'),
                               ('machine-learning', 'Machine Learning'),
                               ('deep-learning', 'Deep Learning'),
                               ('casos-estudio', 'Casos de Estudio'),
                               ('opinion', 'Artículo de Opinión')
                           ],
                           validators=[DataRequired()])

    body = CKEditorField("Contenido del Artículo", validators=[DataRequired()])

    # Tags para mejor organización
    tags = StringField("Etiquetas (separadas por comas)",
                       render_kw={"placeholder": "IA, medicina, anestesiología, innovación"})

    submit = SubmitField("Publicar Artículo")


# Create a form to register new users
class RegisterForm(FlaskForm):
    name = StringField("Nombre Completo", validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6)])

    # Campo adicional para profesión/especialidad
    profession = SelectField("Profesión/Especialidad",
                             choices=[
                                 ('', 'Selecciona tu profesión'),
                                 ('medico', 'Médico'),
                                 ('enfermero', 'Enfermero/a'),
                                 ('anestesiologo', 'Anestesiólogo'),
                                 ('investigador', 'Investigador'),
                                 ('estudiante-medicina', 'Estudiante de Medicina'),
                                 ('ingeniero-biomedico', 'Ingeniero Biomédico'),
                                 ('cientifico-datos', 'Científico de Datos'),
                                 ('otro-profesional-salud', 'Otro Profesional de Salud'),
                                 ('otro', 'Otro')
                             ])

    submit = SubmitField("¡Registrarme!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Iniciar Sesión")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comentario", validators=[DataRequired()],
                                 render_kw={"placeholder": "Comparte tu opinión sobre este artículo..."})
    submit = SubmitField("Publicar Comentario")


# Nuevo formulario para contacto más específico
class ContactForm(FlaskForm):
    name = StringField("Nombre Completo", validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Teléfono (opcional)", validators=[Length(max=20)])

    subject = SelectField("Tipo de Consulta",
                          choices=[
                              ('', 'Selecciona un tema'),
                              ('consulta-general', 'Consulta General'),
                              ('compartir-noticia', 'Compartir Noticia de IA'),
                              ('colaboracion', 'Propuesta de Colaboración'),
                              ('conferencia', 'Invitación a Conferencia'),
                              ('feedback', 'Feedback del Blog'),
                              ('entrevista', 'Solicitud de Entrevista'),
                              ('otro', 'Otro')
                          ],
                          validators=[DataRequired()])

    message = TextAreaField("Mensaje", validators=[DataRequired(), Length(min=10, max=1000)],
                            render_kw={"rows": 6, "placeholder": "Escribe tu mensaje aquí..."})

    submit = SubmitField("Enviar Mensaje")


# Formulario para newsletter (futuro)
class NewsletterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    interests = SelectField("Área de Interés Principal",
                            choices=[
                                ('general', 'Todas las áreas'),
                                ('anestesiologia', 'Anestesiología e IA'),
                                ('diagnostico', 'Diagnóstico por IA'),
                                ('cirugía', 'Cirugía Asistida'),
                                ('investigacion', 'Investigación'),
                                ('herramientas', 'Nuevas Herramientas')
                            ])
    submit = SubmitField("Suscribirse")


# Formulario para sugerencias de artículos
class ArticleSuggestionForm(FlaskForm):
    title = StringField("Título Sugerido", validators=[DataRequired(), Length(max=200)])
    url = StringField("URL del Artículo/Noticia", validators=[URL()],
                      render_kw={"placeholder": "https://..."})
    description = TextAreaField("Breve Descripción",
                                validators=[DataRequired(), Length(min=20, max=500)],
                                render_kw={"rows": 4})
    suggested_by = StringField("Tu Nombre", validators=[DataRequired(), Length(max=100)])
    email = StringField("Tu Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Enviar Sugerencia")