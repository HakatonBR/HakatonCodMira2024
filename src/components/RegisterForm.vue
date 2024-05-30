<script>
import Footer from './Footer.vue';
import Header from './Header.vue';
import axios from 'axios';

export default{
    components: {
        Header,
        Footer,
        axios
    },
    props: {
        logo_name: {
            type: String,
            required: true
        },
    },
    data() {
        return {
            error: null,
            user_info: {
                email: "",
                role: "",
                password: "",
            },
            confirm_password: "",
            }
    },
    computed: {
        is_password_confirmed(){
            return this.user_info.password === this.confirm_password;
        },
        validateEmail() {
            var re = /\S+@\S+\.\S+/;
            return re.test(this.user_info.email);
        },
        is_good_password(){
            var re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;
            return re.test(this.user_info.password);
        }
    },
    methods: {
        register(){
            if(!this.validateEmail) {
                this.error = "Некорректный email";
                return;
            }
            // if(axios.get('#')) {
            //     this.error = "Пользователь с таким email уже существует";
            //     return;
            // }
            if(!this.is_good_password) {
                this.error = "Пароль должен содержать хотя бы одну цифру, одну маленькую и одну большую букву, и быть длиннее 8 символов";
                return;
            }
            if(!this.is_password_confirmed) {
                this.error = "Пароли не совпадают";
                return;
            }
            this.error = null;
            // axios.post(`#`, [this.user_info]) // add the link
        },
    }

}
</script>

<template>
    <Header :logo_name="this.logo_name"></Header>
    <div class="container">
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
                <input type="email" class="registration-row-input" required v-model="this.user_info.email">
            </div>
            <div class="registration-row">
                <h3 class="registration-row-title">Роль</h3> 
                <div class="select-wrapper">
                    <select class="registration-row-select registration-row-input" required v-model="this.user_info.role">
                        <option class="registration-row-select-option">Employe</option>
                        <option class="registration-row-select-option">HR</option>
                    </select>
                </div>
            </div>
            <div class="registration-row">
                <h3 class="registration-row-title">Пароль</h3> 
                <input type="password" class="registration-row-input" required v-model="this.user_info.password">
            </div>
            <div class="registration-row">
                <h3 class="registration-row-title">Подтверждение пароля</h3> 
                <input type="password" class="registration-row-input" required v-model="this.confirm_password">
            </div>
            <input type="submit" class="registration-submit" value="Зарегистрироваться" @click="register()">
            <div class="registration-row row">
                <p class="register-signin">
                    <pre>Если у вас есть аккаунт <a href="#" class="register-signin-url">авторизуйтесь</a></pre>
                </p>
            </div>
        </form>
        <section class="error-section">
            <p class="error">{{ error }}</p>
        </section>
    </div>
    <Footer :logo_name="this.logo_name"></Footer>
</template>

<style scoped>

.container{
    justify-content: center;
    align-items: center;
    width: 100%;
}

.registration-title{
    margin: 10px;
    font-size: 30px;
}

a{
    color: #ff96a6;
    text-decoration: none;
}

a:hover{
    color: 1px solid #fd6e8c;
    translate: 300ms;
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
    border-radius: 50px;
    background-color: #fdf0f0;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 576px;
}

.registration-row-title{
    margin-top: 30px;
    margin-bottom: 10px;
}

.registration-row-input{
    padding: 10px;
    border-radius: 30px;
    border: 1px solid transparent;
    width: 500px;
    outline: none;
}

.registration-row-input:hover, .registration-row-input:active, .registration-row-input:focus{
    border: 1px solid #fd6e8c;
    translate: 300ms;
}

.registration-row-select{
    width: 524px;
    background-color: white;
}

.registration-row-select-option{
    width: 524px;
    background-color: white;
}

.register-signin{
    text-align: center;
    display: block;
}

.registration-submit{
    margin-top: 50px;
    margin-bottom: 30px;
    cursor: pointer;
    padding: 10px;
    border-radius: 30px;
    color: white;
    background-color: #ff96a6;
    border: none;
    width: 524px;
    height: 60px;
}

.registration-submit:hover{
    background-color: #fd6e8c;
    transition: 300ms;
}

.error-section{
    margin-top: 20px;
    display: flex;
    justify-content: center;
}

.error-section{
    text-wrap: wrap;
    display: flex;
    padding: 20px;
    width: 576px;
    border-radius: 30px;
    background-color: red;
}

.error{
    color: white;
}
</style>