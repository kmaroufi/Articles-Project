# Articles-Project

راهکار استفاده شده برای بهینه نمودن محاسبه ی میانگین امتیازها:

برای محاسبه ی تعداد و میانگین امتیاز هر مطلب می توان هر بار که درخواستی برای نمایش لیست مطلب ها به سرور ارسال می شود، آن ها را از روی جدول ArticleRating محاسبه نمود.
اما همانطور که مشخص است این کار هزینه ی پردازشی زیادی دارد و حتی در صورت عدم تغییر در امتیازهای یک مطلب، دوباره نیاز به محاسبه ی مجدد آن در درخواست های بعدی وجود دارد.

دلیل این امر normalize بودن اطلاعات ذخیره شده درون دیتابیس می باشد. هنگامی که مفهوم بهینگی اهمیت پیدا کند، راهکار موجود، denormalize نمودن اطلاعات درون دیتابیس است.
برای این کار روشهای متعددی وجود دارد که برای مثال می توان به بهره مندی از materialized views در دیتابیس اشاره نمود.

در این پروژه به دلیل حفظ سادگی و همچنین زمان محدود 3 ساعت، از دو فیلد درون خود مدل Article برای بهینه نمودن محاسبه ی تعداد و میانگین امتیاز ها استفاده شده است.
