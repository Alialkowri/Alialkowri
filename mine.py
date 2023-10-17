

from odoo_api import models, fields, api

# تعريف النموذج الخاص بالعميل
class Customer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    name = fields.Char('Name')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    # يمكنك إضافة المزيد من الحقول هنا

# الاتصال بخادم Odoo
url = 'https://accounts.odoo.com/ar/web/login'
db = 'edu-a6'
username = 'Ali shaher alkori'
password = '123456'

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
uid = models.execute_kw(db, uid, password, 'res.partner', 'search', [[]])

# قراءة بيانات العملاء
customers = models.execute_kw(db, uid, password, 'res.partner', 'read', [uid], {'fields': ['name', 'email', 'phone']})

# طباعة بيانات العملاء
for customer in customers:
    print('Name:', customer['name'])
    print('Email:', customer['email'])
    print('Phone:', customer['phone'])
    print('-------------------')


#يرجى ملاحظة أنه يجب استبدال http://localhost بعنوان URL الصحيح لخادم Odoo الخاص بك، و my_database بقاعدة البيانات الصحيحة، و admin و admin بمعلومات اعتماد حساب Odoo الصحيحة.

#هذا مجرد مثال بسيط يوضح كيفية الاتصال بخادم Odoo وقراءة بيانات من جدول العملاء. يمكنك استخدام مكتبة Odoo للقيام بالمزيد من العمليات مثل إنشاء وتعديل السجلات، والبحث في البيانات، وإنشاء تقارير، وغيرها.

#يرجى ملاحظة أنه يمكن أيضًا استخدام واجهة برمجة التطبيقات (API) الخاصة بـ Odoo للوصول إلى البيانات. يمكنك الاطلاع على وثائق Odoo API للحصول على مزيد من المعلومات حول كيفية استخدامها.