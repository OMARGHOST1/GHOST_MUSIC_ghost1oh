# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبا عزيزي [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) اهلا بيك سورس GHOST  يتيح لك تشغيل الموسيقى والفيديو في مجموعات من خلال المكالمات في الجروبات الجديده في  TELEGRAM**

💡 **اكتشف جميع أوامر الروبوت وكيفية عملها من خلال النقر فوق » 📚 زر الاوامر!**

🔖 **لمعرفة كيفية استخدام هذا الروبوت ، الرجاء النقر فوق » ❓ زر الدليل الاساسي!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضـف الـبـوت لـ مـجـمـوعـتـك ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" الدليل الاساسي", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton(" الاوامر", callback_data="cbcmds"),
                    InlineKeyboardButton(" مطور البوت", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        " المطور فوديكا يبني", url=f"https://t.me/vod_ik_ax"
                    ),
                    InlineKeyboardButton(
                        " قناة السورس", url=f"https://t.me/GH_OS_T_M1"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        " مطور السورس", url="https://t.me/UU_O_M_AR"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **الدليل الأساسي لاستخدام هذا الروبوت:**

1.) **اولا, أضفني الي مجموعتك.**
2.) **بعد ذلك, قم برفعي مشرف ومنحي جميع الصلاحيات.**
3.) **بعد ترقيتي, اكتب  /reload في المجموعه لتحديث قايمه المشرفين.**
3.) **اضف @{ASSISTANT_NAME}  الي مجموعتك او اكتب /userbotjoin ادعوه الحساب المساعد.**
4.) **قم بتشغيل المكالمه اولا قبل تشغيل الفيديو /الاغاني.**
5.) **في بعض الاحيان, يمكنك أن تساعدك اعاده تحميل البوت بواسطه امر /reload في إصلاح بعض الأخطاء.**

📌 **اذا لم ينضم الحساب المساعد للمكالمه, فتأكد من تشغيل المكالمه بالفعل , او اكتب /userbotleave then type /userbotjoin مره اخرى.**

💡 **اذا لديك اسئله حول هذا البوت , فيمكنك اخبارنا من خلال جروب الدعم الخاص بي هنا: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **اضغط على الازرار التاليه لمعرفه الاوامر     SOURCE GHOST !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامر الادمن", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 اوامر المطورين", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 الاوامر الاساسيه", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 الرجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 هذه هي الاوامر الاساسيه:

» /mplay (اسم الاغنيه /الرابط) - تشغيل اغاني في الكول
» /vplay (اسم الفيديو /الرابط) - تشغيل الفيديو في الكول 
» /vstream - تشغيل فيديو مباشر من اليوتيوب/الرابط
» /playlist - عرض قائمه الاغاني
» /video (query) - تحميل فيديو من اليوتيوب
» /song (query) - تحميل الاغنيه من اليوتيوب
» /search (query) - البحث في رابط فيديو يوتيوب

» /ping - يظهر حاله بينج البوت
» /uptime - يظهر لك حاله التشغيل
» /alive - يعرض لك معلومات البوت (في المجموعه)

   SOURCE GHOST

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اوامر الادمن ياقلبي:

» /pause - إيقاف التشغيل مؤقت
» /resume - استئناف التشغيل
» /skip - تخطي الي التالي
» /stop - إيقاف التشغيل
» /vmute - لكتم البوت
» /vunmute - لإلغاء كتم البوت
» /volume `1-200` - الرقم القياسي لضبط الصوت (خاص بالادمن)
» /reload - لتحديث البوت وقائمه الادمن
» /userbotjoin - لدعوه الحساب المساعد 
» /userbotleave - لاخرج الحساب المساعد 

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اوامر المطورين:

» /rmw - تنظيف كافة الملفات الخام
» /rmd - تنظيف كافة الملفات التي تم تنزيلها
» /sysinfo - إظهار معلومات النظام
» /update - تحديث البوت ل اخر نسخه
» /restart - اعاده تشغيل البوت
» /leaveall - خروج الحساب المساعد من جميع الجروبات

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الرجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 الادمن بس بقلبي الي يقدروا يستعملوا الازرار دي!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الاعدادات** {query.message.chat.title}\n\n⏸ : إيقاف التشغيل مؤقتا\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : إيقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 اغلاق", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ قائمه التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه رول يدوس على الازرار ي قلبي💕!", show_alert=True)
    await query.message.delete()
