#coding:utf-8

from gluon import current  # Dependência básica (porém desnecessária do web2py)


class EmailBasico(object):

    def __init__(self, mail=current.mail, render=current.response.render):
        """
        A classe ``EmailBasico`` trata estritamente de envio de emails
        Utilizada a classe  nativa de email de gluon.tools.

        :type mail: gluon.tools.Mail
        :param mail: Classe Mail que enviará os emails de fato. (current.mail)
        :type render: callable que aceita dois parâmetros (a,b), onde a é uma str/enderaço de uma view e b é um contexto passado para a mesma.
        :param render Renderizador que gera a mensagem do email.
        """
        self.mail = mail
        self.render = render
        self.reply_to = self.mail.settings.sender
        self.subject_sender = "[DTIC]"

    def send_email(self, **args):

        if not args.has_key('reply_to'):
            args['reply_to'] = self.reply_to

        return self.mail.send(**args) # TODO Mandar para uma queue??

    def monta_assunto(self, subject):
        return self.subject_sender + " - " + subject