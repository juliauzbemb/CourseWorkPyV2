import vk
import ya
import os

if __name__ == "__main__":
    vk_photo = vk.VkPhotoOwner('552934290')
    vk_photo.download_vk_photos()
    with open('ya_token.txt', 'r') as file:
        ya_token = file.read().strip()
    yandex_client = ya.Yandex(ya_token)
    yandex_client.backup('Backup2', os.path.abspath('Photo_Album'))
