@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.name.data.lower()
        surname = form.surname.data.lower()
        email = form.email.data
        user = User(name=name, surname=surname, email=email)
        if User.query.filter(User.email == email).first():
            flash(f'Пользователь с e-mail {email} уже существует')
            return redirect(url_for('registration'))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('registration'))
    return render_template('registration.html', form=form)