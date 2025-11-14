# Student Clubs

from pyscript import display  # type: ignore

Art_Club = {'ꜱʜᴀʟᴀɴɪᴇ ɢᴀʀᴀʙɪʟᴇꜱ', 'ᴀᴍᴀɴᴅᴀ ʏᴀᴏ', 'ɴɪʟᴢᴀ ᴄᴀʟᴀɴɢʟᴀɴɢ'}
COCC = {'ᴀɪꜱʜᴀ ʟᴇᴅᴇꜱᴍᴀ', 'ᴋᴏʙʏ ʙᴀʏʟᴏɴ', 'ᴍᴀʀʏᴀᴍ ʟᴇᴅᴇꜱᴍᴀ'}

display('ᴀʀᴛ ᴄʟᴜʙ ᴍᴇᴍʙᴇʀꜱ:', target='output')
display(Art_Club, target='output')
display('ᴄᴏᴄᴄ ᴍᴇᴍʙᴇʀꜱ:', target='output')
display(COCC, target='output')

display('(ᴀᴛ ʟᴇᴀꜱᴛ ᴏɴᴇ ᴄʟᴜʙ):', target='output')
display(Art_Club | COCC, target="output")

display('(ʙᴏᴛʜ ᴄʟᴜʙꜱ):', target='output')
display(Art_Club & COCC, target='output')

display('ᴏɴʟʏ ɪɴ ᴀʀᴛ ᴄʟᴜʙ:', target='output')
display(Art_Club - COCC, target='output')

display('ᴏɴʟʏ ɪɴ ᴄᴏᴄᴄ:', target='output')
display(COCC - Art_Club, target='output')

display('ᴇxᴀᴄᴛʟʏ ᴏɴᴇ ᴄʟᴜʙ:', target='output')
display(Art_Club ^ COCC, target='output')
