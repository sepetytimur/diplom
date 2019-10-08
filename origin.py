import sys
import time
from VkAPI import VkAPI
#vk = VkAPI('171691064')

def get_list_friends_groups( vk, friend_ids):
    i = 0
    count = len(friend_ids)
    result = []
    for friend_id in friend_ids:
        group_list = vk.get_group_list(friend_id)

        if 'error' in group_list:
            i = i + 1
            continue

        result += group_list['response']['items']

        i = i + 1
        print('', end='\r')
        print('complete : {:.2%}'.format(i / count), end='')
        time.sleep(0.4)
    return result


def main():
    vk = VkAPI('171691064')
    friends_list = vk.get_friend_list()['response']['items']
    group_list = vk.get_group_list()
    all_friends_groups = get_list_friends_groups(vk, friends_list)
    result_groups_without_friends = set(group_list['response']['items']) - set(all_friends_groups)
    print(result_groups_without_friends)


if __name__ == '__main__':
    main()
