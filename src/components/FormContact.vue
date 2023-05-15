<template>
    <div class="box-contact pt-14">
        <section class="text-gray-600 body-font py-28">
            <div class="title-font sm:text-3xl text-2xl mb-0 font-black text-text1 py-2">Contact us</div>
            <div class="lg:py-4 px-4 mx-auto max-w-screen-fix">
                <form action="#" class="space-y-2">
                    <div>
                        <input type="text" placeholder="Topic" v-model="form.name"
                            class="text-text1 text-sm font-sans rounded-lg focus:ring-primary-500 focus:border-primary-500 block w-full p-3"
                            required />
                    </div>
                    <div>
                        <input type="email" placeholder="Email" v-model="form.email" :class="{ 'red-border': wrongEmail }"
                            class="block p-3 px-52 w-full text-sm text-text1 font-sans rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500"
                            required>
                    </div>
                    <div class="sm:col-span-2">
                        <textarea v-model="form.message" placeholder="Message" rows="6"
                            class="block p-3 px-52 w-full text-sm text-text1 font-sans rounded-lg border border-gray-300 focus:ring-primary-500 focus:border-primary-500"></textarea>
                    </div>
                    <button type="submit"
                        class="submit-button py-3 px-56 text-sm font-medium text-white text-center border rounded-lg bg-btn1 w-full hover:bg-btn11 focus:ring-primary-300"
                        @click="sendMessage">
                        <div v-if="!sending">
                            {{ textButton }}
                        </div>
                        <div v-else>Processing...</div>
                    </button>
                </form>
            </div>
        </section>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "FromContact",
    data() {
        return {
            form: {
                name: "",
                email: "",
                message: "",
            },
            wrongEmail: false,
            textButton: "Send message",
            sending: false,
        };
    },
    methods: {
        sendMessage() {
            console.log(this.form);
            if (
                this.form.name == "" ||
                this.form.email == "" ||
                this.form.message == ""
            ) {
                alert("Please fill out the form");
                return;
            }
            this.validateEmail();
            if (this.wrongEmail) {
                return;
            }
            this.sending = true;
            // this.textButton = "Sending...";
            axios
                .post("http://localhost:5000/contact", this.form) //Nest 8000, Flask 5000
                .then((res) => {
                    if (res.data.message == "success") {
                        alert("Success");
                        this.sending = false;
                    }
                    // this.textButton = "Send message";
                })
                .catch(() => {
                    this.sending = false;
                    // this.textButton = "Send message";
                    alert("server failure");
                });
        },
        validateEmail() {
            if (!/^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$/.test(this.form.email)) {
                this.wrongEmail = true;
                alert("Please type correct email");
            } else {
                this.wrongEmail = false;
            }
        },
    },
};
</script>

<style scoped></style>