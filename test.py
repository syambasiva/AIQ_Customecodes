my_url_list = ['http://www.stackoverflow.com','http://www.whitehouse.gov']

link_list = []
for each_url in my_url_list:
    link_string = '<a href = "'
    link_string = link_string + each_url
    link_string = link_string +'">'
    link_name = each_url.split('.')[1]
    link_string = link_string + link_name + '</a><br>\n'
    link_list.append(link_string)


print(link_list)