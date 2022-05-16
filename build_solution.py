top_template = open('./templates/top_template.html').read()
bottom_template = open('./templates/bottom_template.html').read()

content = open('./content/middle_index.html').read()
index_html = top_template + content + bottom_template
open('./docs/index.html', 'w+').write(index_html)

content = open('./content/middle_about.html').read()
about_html = top_template + content + bottom_template
open('./docs/about.html', 'w+').write(about_html)

content = open('./content/middle_contact.html').read()
contact_html = top_template + content + bottom_template
open('./docs/contact.html', 'w+').write(contact_html)

content = open('./content/middle_portfolio.html').read()
portfolio_html = top_template + content + bottom_template
open('./docs/portfolio.html', 'w+').write(portfolio_html)
