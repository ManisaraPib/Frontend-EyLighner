<template>
    <div class="fixed flex w-full bg-gradient-to-r from-navbar1 to-navbar2 animated" style="z-index: 4;"
        :class="{ 'scrolled': !view.atTopOfPage }">
        <nav class="
                                                                container
                                                                px-4
                                                                py-3.5
                                                                mx-auto
                                                                md:flex md:justify-between md:items-center
                                                                ">
            <div class="flex items-center justify-between">
                <router-link to="/" class="
                                                                    text-xl
                                                                    font-black
                                                                    text-white
                                                                    md:text-xl
                                                                    hover:text-indigo-400
                                                                  ">
                    <div class="flex items-center justify-between flex-wrap">
                        <img src="../image/logo.png" class="eln-logo" />
                        <span class="px-3">EyLighner</span>
                    </div>
                </router-link>

                <div @click="toggleNav" class="flex md:hidden">
                    <button type="button" class="
                                                                      text-gray-100
                                                                      hover:text-gray-400
                                                                      focus:outline-none focus:text-gray-400
                                                                    ">
                        <svg viewBox="0 0 24 24" class="w-6 h-6 fill-current">
                            <path fill-rule="evenodd"
                                d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z">
                            </path>
                        </svg>
                    </button>
                </div>
            </div>

            <ul :class="showMenu ? 'flex' : 'hidden'" class="
                                                                  flex-col
                                                                  mt-8
                                                                  space-y-4
                                                                  md:flex md:space-y-0 md:flex-row md:items-center md:space-x-5 md:mt-0
                                                                ">
                <p class="text-white font-semibold md:text-base">Eye alignment</p>
                <div class="box bg-white md:px-0.5 md:py-3 sm:px-10 sm:py-0.5"></div>
                <a class="text-gray-100 font-light hover:text-neutral-400" href="/">Home</a>
                <a class="text-gray-100 font-light hover:text-neutral-400" href="/contact">Contact Us</a>
            </ul>
        </nav>
    </div>
</template>

<script>
import { ref } from 'vue';
export default {
    name: "NavBar",
    setup() {
        let showMenu = ref(false);
        const toggleNav = () => (showMenu.value = !showMenu.value);
        return { showMenu, toggleNav };
    },
    data() {
        return {
            view: {
                atTopOfPage: true
            }
        }
    }, beforeMount() {
        window.addEventListener('scroll', this.handleScroll);
    },
    methods: {
        // the function to call when the user scrolls, added as a method
        handleScroll() {
            // when the user scrolls, check the pageYOffset
            if (window.pageYOffset > 0) {
                // user is scrolled
                if (this.view.atTopOfPage) this.view.atTopOfPage = false
            } else {
                // user is at top of page
                if (!this.view.atTopOfPage) this.view.atTopOfPage = true
            }
        }
    },
};


</script>

<style scoped>
.eln-logo {
    width: 49px;
    height: 28px;
}
</style>