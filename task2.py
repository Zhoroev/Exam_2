text_1 = 'Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colorless.But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.'
text = text_1.lower()


def func(text):
    count_s = 0
    count_t = 0
    for i in text:
        if i == 's':
            count_s += 1
        elif i == 't':
            count_t += 1
    print(f's - {count_s}\nt - {count_t}')


func(text)

word = 'advert'
final_text = text.replace('advert', 'ADVERT')
print(final_text)
