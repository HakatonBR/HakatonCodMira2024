<script>
import Footer from './components/Footer.vue';
import Header from './components/Header.vue';
import RegisterForm from './components/RegisterForm.vue';

export default{
    components: {
        Header,
        Footer,
        RegisterForm
    },
    data() {
        return {
            logo_name: "IP-position"
        }
    },
    computed: {
    },
    methods: {
        
    }
}
</script>

<template>
    <Header :logo_name="this.logo_name"></Header>
    <RegisterForm :logo_name="this.logo_name"></RegisterForm>
    <Footer :logo_name="this.logo_name"></Footer>
</template>

<style>
</style>
