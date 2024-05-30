<script>
import Header from './Header.vue';
import Footer from './Footer.vue';

export default{
    components: {
        Header,
        Footer
    },
    props: {
        logo_name: {
            type: String,
            required: true
        }
    }
}
</script>

<template>
    <Header :logo_name="this.logo_name"></Header>
    <form class="registration-form">
        <div class="row">
            <img src="" alt="" class="registration-logo"> 
            <h1 class="registration-title">
                Регистрация
            </h1>
        </div>
        <div class="row">
            <hr class="registration-divider">
        </div>
        <div class="registration-row">
            <h3 class="registration-row-title">Почта</h3> 
            <input type="email" class="registration-row-input">
        </div>
        <div class="registration-row">
            <h3 class="registration-row-title">Роль</h3> 
            <select class="registration-row-select">
                <option class="registration-row-select-option">Employe</option>
                <option class="registration-row-select-option">HR</option>
            </select>
        </div>
        <div class="registration-row">
            <h3 class="registration-row-title">Пароль</h3> 
            <input type="password" class="registration-row-input">
        </div>
        <div class="registration-row">
            <h3 class="registration-row-title">Подтверждение пароля</h3> 
            <input type="password" class="registration-row-input">
        </div>
        <input type="submit" class="registration-submit" value="Зарегистрироваться">
        <div class="registration-row row">
            <p class="register-signin">
                <pre>Если у вас есть аккаунт <a href="#" class="register-signin-url">авторизуйтесь</a></pre>
            </p>
        </div>
    </form>
    <Footer :logo_name="this.logo_name"></Footer>
</template>

<style scoped>
.registration-title{
    margin: 10px;
    font-size: 30px;
}

a{
    color: #ff96a6;
    text-decoration: none;
}

.registration-divider{
    margin-top: 20px;
    justify-content: center;
    height: 4px;
    width: 100px;
    background-color: #ff96a6;
    border: none;
}

.row{
    display: flex;
    justify-content: center;
}

.registration-form{
    margin-top: 50px;
    padding: 30px;
    border-radius: 5px;
    border: 1px solid #ff96a6;
}

.registration-row-title{
    margin-top: 30px;
    margin-bottom: 10px;
}

.registration-row-input{
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ff96a6;
    width: 500px;
}

.registration-row-select{
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ff96a6;
    background-color: white;
    width: 524px;
}

.register-signin{
    text-align: center;
    display: block;
}

.registration-submit{
    margin-top: 30px;
    margin-bottom: 30px;
    cursor: pointer;
    padding: 10px;
    border-radius: 5px;
    color: white;
    background-color: #ff96a6;
    border: none;
    width: 524px;
}
</style>