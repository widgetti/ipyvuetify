- To release a new version of ipyvuetify on PyPI:

Update \_version.py (set release version, remove 'dev')
git add the \_version.py file and git commit
`python setup.py sdist upload`
`python setup.py bdist_wheel upload`
`git tag -a X.X.X -m 'comment'`
Update \_version.py (add 'dev' and increment minor)
git add and git commit
git push
git push --tags

- To release a new version of jupyter-vuetify on NPM:

```
# clean out the `dist` and `node_modules` directories
git clean -fdx
npm install
npm publish
```
