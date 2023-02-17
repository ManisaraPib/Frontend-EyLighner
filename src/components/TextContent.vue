<template>
    <div class="box-contect">
        <section class="text-gray-600 body-font mx-auto items-center" id="main">
            <div class="container mx-auto flex px-40 pt-24 pb-2 md:flex-row flex-col">
                <div
                    class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 text-justify">
                    <div class="title-font sm:text-3xl text-3xl font-black text-text1">EyLighner
                    </div>
                    <div class="leading-tighter text-text1 font-semibold text-sm font-sans">in version 1</div>
                    <div class="text-md sm:text-left leading-normal flex-start text-text2 font-sans">
                        The
                        EyLighner project uses image processing to create an algorithm, the composition<br> is aligned
                        and measures automatically the distance of the ability to open the eyes.
                    </div>
                    <a class="flex justify-left py-2" href="https://pubmed.ncbi.nlm.nih.gov/34581296/" target="_blank">
                        <button
                            class="inline-flex items-center text-white bg-btn2 border-lg py-2 px-6 focus:outline-none hover:bg-btn22 rounded-lg text-lg">Tutorial
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-5 h-5 ml-1">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25" />
                            </svg>
                        </button>
                    </a>
                    <div class="text-md text-text1 font-sans font-medium mt-3 pb-0">Select image to upload and press
                        next:
                    </div>
                </div>
                <div class="logo-img">
                    <img class="object-cover md:w-40 ss:w-0 rounded" alt="hero" src="../image/logo-contect.png">
                </div>
            </div>
        </section>
        <section class="text-gray-600 body-font mx-auto items-center" id="des" hidden>
            <div class="container mx-auto flex px-40 pt-24 md:flex-row flex-col">
                <div
                    class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 text-justify">
                    <div class="title-font sm:text-2xl text-2xl font-black text-text1">Description
                    </div>
                    <div class="text-md sm:text-left leading-normal flex-start text-text2 font-sans">
                        Please select pairs of outcome by clicking in the box you wish to compare. The model will
                        compose the images into alignment and display in the form of comaprison. And the vertical
                        options
                        will be the ones on the left and top. Horizontal options are shown on the right and below.
                    </div>
                </div>
            </div>
        </section>

        <div class="relative bg-bginput h-48 w-120 mx-auto overflow-hidden rounded-2xl mb-3 mdd:h-96 md:h-0 ss:h-0"
            id="div_main">
            <form>

                <!--  1  -->
                <div class="w-120 bg-[bginput] rounded-lg flex" style="height: 25rem;" id="f_0">
                    <div class="w-20 mr-auto flex items-center h-full">
                        <div class="ml-auto mr-auto">

                        </div>
                    </div>
                    <div class="w-8/12 h-80 mr-auto ml-auto mt-3 bg-white rounded-lg shadow-md">
                        <div class="text-left ml-10 mr-10 mt-4">
                            <div
                                class="flex flex-row items-center border-b border-zinc-400 py-0 w-44 hover:border-zinc-500">
                                <input
                                    class="pb-1 block appearance-none bg-transparent border-none w-full text-gray-700 font-sans font-medium mr-3 py-0 px-2 leading-tight focus:outline-none"
                                    type="text" placeholder="Follow up period" id="text_follow_0" v-model="text_follow_1"
                                    oninput="javascript: if (text_follow_1.length > this.maxLength) text_follow_1 = text_follow_1.slice(0, this.maxLength);"
                                    maxlength="14" aria-label="Follow up" @change="input_follow">
                                <svg class="h-6 w-6 text-zinc-400 hover:text-zinc-500" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                                </svg>
                            </div>
                            <div class="flex text-xxs text-text1 text-zinc-400 font-sans mt-1"
                                :style="{ color: text_follow_1.length == 14 ? 'red' : 'gray' }">Please input your
                                following up
                                period above
                                within
                                <div class="flex flex-row ml-1 mr-1 input-group-addon" v-text="(14 - text_follow_1.length)"
                                    :style="{ color: text_follow_1.length == 14 ? 'red' : 'gray' }"></div>characters
                            </div>
                            <div class="flex h-full mt-2">
                                <div class="flex items-center justify-center w-2/4 h-full mr-1 relative"
                                    @dragover="dragover" @drop="drop($event, 'f0_1')">
                                    <label for="dropzone1-file_f0"
                                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-bgddimg hover:bg-zinc-600/10"
                                        id="label_f0_1">
                                        <div class="flex flex-col items-center justify-center pt-4 pb-6 font-sans">
                                            <svg class="h-7 w-7 text-zinc-500" viewBox="0 0 24 24" fill="none"
                                                stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                                                <circle cx="12" cy="12" r="3" />
                                            </svg>
                                            <p class="mb-0 text-sm text-zinc-500">Open Both Eyes
                                                Image</p>
                                            <div class="flex justify-start">
                                                <p class="text-xs text-zinc-400">Drop your image here, or</p>
                                                <p class="text-xs text-zinc-400 underline ml-1">browse</p>
                                            </div>
                                        </div>
                                        <input accept="image/png, image/jpeg, image/jpg" id="dropzone1-file_f0" type="file"
                                            class="hidden" @change="onFile_($event, 'f0_1')" />
                                    </label>
                                    <img :src="image_f0_1" class="w-full h-64 border-2 border-dashed rounded-lg"
                                        id="img_f0_1" hidden />
                                    <div class="absolute right-3 top-2" id="btn_f0_1" hidden>
                                        <button type="button" @click="cancel('f0_1')">
                                            <svg class="h-5 w-5 text-red-700 hover:text-red-900" viewBox="0 0 24 24"
                                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <circle cx="12" cy="12" r="10" />
                                                <line x1="15" y1="9" x2="9" y2="15" />
                                                <line x1="9" y1="9" x2="15" y2="15" />
                                            </svg>
                                        </button>
                                    </div>
                                </div>

                                <div class="flex items-center justify-center w-2/4 h-full ml-1 relative"
                                    @dragover="dragover" @drop="drop($event, 'f0_2')">
                                    <label for="dropzone2-file_f0"
                                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-bgddimg hover:bg-zinc-600/10"
                                        id="label_f0_2">
                                        <div class="flex flex-col items-center justify-center pt-4 pb-6 font-sans">
                                            <img src="../image/close-eye.png" width="30px" alt="" srcset="">
                                            <p class="mb-0 text-sm text-zinc-500">Close Both Eyes Image
                                            </p>
                                            <div class="flex justify-start">
                                                <p class="text-xs text-zinc-400 ">Drop your image here, or</p>
                                                <p class="text-xs text-zinc-400 underline ml-1">browse</p>
                                            </div>
                                        </div>
                                        <input accept="image/png, image/jpeg, image/jpg" id="dropzone2-file_f0" type="file"
                                            class="hidden" @change="onFile_($event, 'f0_2')" />
                                    </label>
                                    <img :src="image_f0_2" class="w-full h-64 border-2 border-dashed rounded-lg"
                                        id="img_f0_2" hidden />
                                    <div class="absolute right-3 top-2" id="btn_f0_2" hidden>
                                        <button type="button" @click="cancel('f0_2')">
                                            <svg class="h-5 w-5 text-red-700 hover:text-red-900" viewBox="0 0 24 24"
                                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <circle cx="12" cy="12" r="10" />
                                                <line x1="15" y1="9" x2="9" y2="15" />
                                                <line x1="9" y1="9" x2="15" y2="15" />
                                            </svg>
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <p class="flex justify-end text-xxs text-zinc-500 font-sans mt-2">Page 1</p>
                        </div>

                    </div>
                    <button type="button"
                        class="w-20 ml-auto flex items-center h-full hover:bg-[#B2AAAA] active:bg-[#B2AAAA] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                        @click="next">
                        <div class="ml-auto mr-auto">
                            <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6" />
                            </svg>
                        </div>
                    </button>
                </div>

                <!-- 2 -->
                <div class="w-120 bg-[bginput] rounded-lg flex" style="height: 25rem;" id="f_1" hidden>
                    <button type="button"
                        class="w-20 mr-auto flex items-center h-full hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                        @click="back">
                        <div class="ml-auto mr-auto">
                            <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="15 18 9 12 15 6" />
                            </svg>
                        </div>
                    </button>
                    <div class="w-8/12 h-80 mr-auto ml-auto mt-3 bg-white rounded-lg shadow-md">
                        <div class="text-left ml-10 mr-10 mt-4">
                            <div
                                class="flex flex-row items-center border-b border-zinc-400 py-0 w-44 hover:border-zinc-500">
                                <input
                                    class="pb-1 block appearance-none bg-transparent border-none w-full text-gray-700 font-sans font-medium mr-3 py-0 px-2 leading-tight focus:outline-none"
                                    type="text" placeholder="Follow up period" id="text_follow_0" v-model="text_follow_2"
                                    oninput="javascript: if (text_follow_2.length > this.maxLength) text_follow_2 = text_follow_2.slice(0, this.maxLength);"
                                    maxlength="14" aria-label="Follow up" @change="input_follow">
                                <svg class="h-6 w-6 text-zinc-400 hover:text-zinc-500" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                                </svg>
                            </div>
                            <div class="flex text-xxs text-text1 text-zinc-400 font-sans mt-1"
                                :style="{ color: text_follow_2.length == 14 ? 'red' : 'gray' }">Please input your
                                following up
                                period above
                                within
                                <div class="flex flex-row ml-1 mr-1 input-group-addon" v-text="(14 - text_follow_2.length)"
                                    :style="{ color: text_follow_2.length == 14 ? 'red' : 'gray' }"></div>characters
                            </div>
                            <div class="flex h-full mt-2">
                                <div class="flex items-center justify-center w-2/4 h-full mr-1 relative"
                                    @dragover="dragover" @drop="drop($event, 'f1_1')">
                                    <label for="dropzone1-file_f1"
                                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-bgddimg hover:bg-zinc-600/10"
                                        id="label_f1_1">
                                        <div class="flex flex-col items-center justify-center pt-4 pb-6 font-sans">
                                            <svg class="h-7 w-7 text-zinc-500" viewBox="0 0 24 24" fill="none"
                                                stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                                                <circle cx="12" cy="12" r="3" />
                                            </svg>
                                            <p class="mb-0 text-sm text-zinc-500">Open Both Eyes Image
                                            </p>
                                            <div class="flex justify-start">
                                                <p class="text-xs text-zinc-400">Drop your image here, or</p>
                                                <p class="text-xs text-zinc-400 underline ml-1">browse</p>
                                            </div>
                                        </div>
                                        <input accept="image/png, image/jpeg, image/jpg" id="dropzone1-file_f1" type="file"
                                            class="hidden" @change="onFile_($event, 'f1_1')" />
                                    </label>
                                    <img :src="image_f1_1" class="w-full h-64 border-2 border-dashed rounded-lg"
                                        id="img_f1_1" hidden />
                                    <div class="absolute right-3 top-2" id="btn_f1_1" hidden>
                                        <button type="button" @click="cancel('f1_1')">
                                            <svg class="h-5 w-5 text-red-700 hover:text-red-900" viewBox="0 0 24 24"
                                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <circle cx="12" cy="12" r="10" />
                                                <line x1="15" y1="9" x2="9" y2="15" />
                                                <line x1="9" y1="9" x2="15" y2="15" />
                                            </svg>
                                        </button>
                                    </div>
                                </div>

                                <div class="flex items-center justify-center w-2/4 h-full ml-1 relative"
                                    @dragover="dragover" @drop="drop($event, 'f1_2')">
                                    <label for="dropzone2-file_f1"
                                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-bgddimg hover:bg-zinc-600/10"
                                        id="label_f1_2">
                                        <div class="flex flex-col items-center justify-center pt-4 pb-6 font-sans">
                                            <img src="../image/close-eye.png" width="30px" alt="" srcset="">
                                            <p class="mb-0 text-sm text-zinc-500">Close Both Eyes Image
                                            </p>
                                            <div class="flex justify-start">
                                                <p class="text-xs text-zinc-400 ">Drop your image here, or</p>
                                                <p class="text-xs text-zinc-400 underline ml-1">browse</p>
                                            </div>
                                        </div>
                                        <input accept="image/png, image/jpeg, image/jpg" id="dropzone2-file_f1" type="file"
                                            class="hidden" @change="onFile_($event, 'f1_2')" />
                                    </label>
                                    <img :src="image_f1_2" class="w-full h-64 border-2 border-dashed rounded-lg"
                                        id="img_f1_2" hidden />
                                    <div class="absolute right-3 top-2" id="btn_f1_2" hidden>
                                        <button type="button" @click="cancel('f1_2')">
                                            <svg class="h-5 w-5 text-red-700 hover:text-red-900" viewBox="0 0 24 24"
                                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <circle cx="12" cy="12" r="10" />
                                                <line x1="15" y1="9" x2="9" y2="15" />
                                                <line x1="9" y1="9" x2="15" y2="15" />
                                            </svg>
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <p class="flex justify-end text-xxs text-zinc-500 font-sans mt-2">Page 2</p>
                        </div>

                    </div>
                    <button type="button"
                        class="w-20 ml-auto flex items-center h-full hover:bg-[#B2AAAA] active:bg-[#B2AAAA] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                        @click="next">
                        <div class="ml-auto mr-auto">
                            <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6" />
                            </svg>
                        </div>
                    </button>
                </div>

                <!-- 3 -->
                <div class="w-120 bg-[bginput] rounded-lg flex" style="height: 25rem;" id="f_2" hidden>
                    <button type="button"
                        class="w-20 mr-auto flex items-center h-full hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                        @click="back">
                        <div class="ml-auto mr-auto">
                            <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="15 18 9 12 15 6" />
                            </svg>
                        </div>
                    </button>
                    <div class="w-8/12 h-80 mr-auto ml-auto mt-3 bg-white rounded-lg shadow-md">
                        <div class="text-left ml-10 mr-10 mt-4">
                            <div
                                class="flex flex-row items-center border-b border-zinc-400 py-0 w-44 hover:border-zinc-500">
                                <input
                                    class="pb-1 block appearance-none bg-transparent border-none w-full text-gray-700 font-sans font-medium mr-3 py-0 px-2 leading-tight focus:outline-none"
                                    type="text" placeholder="Follow up period" id="text_follow_0" v-model="text_follow_3"
                                    oninput="javascript: if (text_follow_3.length > this.maxLength) text_follow_3 = text_follow_3.slice(0, this.maxLength);"
                                    maxlength="14" aria-label="Follow up" @change="input_follow">
                                <svg class="h-6 w-6 text-zinc-400 hover:text-zinc-500" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                                </svg>
                            </div>
                            <div class="flex text-xxs text-text1 text-zinc-400 font-sans mt-1"
                                :style="{ color: text_follow_3.length == 14 ? 'red' : 'gray' }">Please input your
                                following up
                                period above
                                within
                                <div class="flex flex-row ml-1 mr-1 input-group-addon" v-text="(14 - text_follow_3.length)"
                                    :style="{ color: text_follow_3.length == 14 ? 'red' : 'gray' }"></div>characters
                            </div>
                            <div class="flex h-full mt-2">
                                <div class="flex items-center justify-center w-2/4 h-full mr-1 relative"
                                    @dragover="dragover" @drop="drop($event, 'f2_1')">
                                    <label for="dropzone1-file_f2"
                                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-bgddimg hover:bg-zinc-600/10"
                                        id="label_f2_1">
                                        <div class="flex flex-col items-center justify-center pt-4 pb-6 font-sans">
                                            <svg class="h-7 w-7 text-zinc-500" viewBox="0 0 24 24" fill="none"
                                                stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                                                <circle cx="12" cy="12" r="3" />
                                            </svg>
                                            <p class="mb-0 text-sm text-zinc-500">Open Both Eyes Image
                                            </p>
                                            <div class="flex justify-start">
                                                <p class="text-xs text-zinc-400">Drop your image here, or</p>
                                                <p class="text-xs text-zinc-400 underline ml-1">browse</p>
                                            </div>
                                        </div>
                                        <input accept="image/png, image/jpeg, image/jpg" id="dropzone1-file_f2" type="file"
                                            class="hidden" @change="onFile_($event, 'f2_1')" />
                                    </label>
                                    <img :src="image_f2_1" class="w-full h-64 border-2 border-dashed rounded-lg"
                                        id="img_f2_1" hidden />
                                    <div class="absolute right-3 top-2" id="btn_f2_1" hidden>
                                        <button type="button" @click="cancel('f2_1')">
                                            <svg class="h-5 w-5 text-red-700 hover:text-red-900" viewBox="0 0 24 24"
                                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <circle cx="12" cy="12" r="10" />
                                                <line x1="15" y1="9" x2="9" y2="15" />
                                                <line x1="9" y1="9" x2="15" y2="15" />
                                            </svg>
                                        </button>
                                    </div>
                                </div>

                                <div class="flex items-center justify-center w-2/4 h-full ml-1 relative"
                                    @dragover="dragover" @drop="drop($event, 'f2_2')">
                                    <label for="dropzone2-file_f2"
                                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-bgddimg hover:bg-zinc-600/10"
                                        id="label_f2_2">
                                        <div class="flex flex-col items-center justify-center pt-4 pb-6 font-sans">
                                            <img src="../image/close-eye.png" width="30px" alt="" srcset="">
                                            <p class="mb-0 text-sm text-zinc-500">Close Both Eyes Image
                                            </p>
                                            <div class="flex justify-start">
                                                <p class="text-xs text-zinc-400 ">Drop your image here, or</p>
                                                <p class="text-xs text-zinc-400 underline ml-1">browse</p>
                                            </div>
                                        </div>
                                        <input accept="image/png, image/jpeg, image/jpg" id="dropzone2-file_f2" type="file"
                                            class="hidden" @change="onFile_($event, 'f2_2')" />
                                    </label>
                                    <img :src="image_f2_2" class="w-full h-64 border-2 border-dashed rounded-lg"
                                        id="img_f2_2" hidden />
                                    <div class="absolute right-3 top-2" id="btn_f2_2" hidden>
                                        <button type="button" @click="cancel('f2_2')">
                                            <svg class="h-5 w-5 text-red-700 hover:text-red-900" viewBox="0 0 24 24"
                                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <circle cx="12" cy="12" r="10" />
                                                <line x1="15" y1="9" x2="9" y2="15" />
                                                <line x1="9" y1="9" x2="15" y2="15" />
                                            </svg>
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <p class="flex justify-end text-xxs text-zinc-500 font-sans mt-2">Page 3</p>
                        </div>

                    </div>
                    <button type="button"
                        class="w-20 ml-auto flex items-center h-full hover:bg-[#B2AAAA] active:bg-[#B2AAAA] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                        @click="next">
                        <div class="ml-auto mr-auto">
                            <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6" />
                            </svg>
                        </div>
                    </button>
                </div>

                <!-- 4 -->
                <div class="w-120 bg-[bginput] rounded-lg flex" style="height: 25rem;" id="f_3" hidden>
                    <button type="button"
                        class="w-20 mr-auto flex items-center h-full hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                        @click="back">
                        <div class="ml-auto mr-auto">
                            <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="15 18 9 12 15 6" />
                            </svg>
                        </div>
                    </button>
                    <div class="w-8/12 h-80 mr-auto ml-auto mt-3 bg-white rounded-lg shadow-md">
                        <div class="text-left ml-10 mr-10 mt-4">
                            <div
                                class="flex flex-row items-center border-b border-zinc-400 py-0 w-44 hover:border-zinc-500">
                                <input
                                    class="pb-1 block appearance-none bg-transparent border-none w-full text-gray-700 font-sans font-medium mr-3 py-0 px-2 leading-tight focus:outline-none"
                                    type="text" placeholder="Follow up period" id="text_follow_0" v-model="text_follow_4"
                                    oninput="javascript: if (text_follow_4.length > this.maxLength) text_follow_4 = text_follow_4.slice(0, this.maxLength);"
                                    maxlength="14" aria-label="Follow up" @change="input_follow">
                                <svg class="h-6 w-6 text-zinc-400 hover:text-zinc-500" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                                </svg>
                            </div>
                            <div class="flex text-xxs text-text1 text-zinc-400 font-sans mt-1"
                                :style="{ color: text_follow_4.length == 14 ? 'red' : 'gray' }">Please input your
                                following up
                                period above
                                within
                                <div class="flex flex-row ml-1 mr-1 input-group-addon" v-text="(14 - text_follow_4.length)"
                                    :style="{ color: text_follow_4.length == 14 ? 'red' : 'gray' }"></div>characters
                            </div>
                            <div class="flex h-full mt-2">
                                <div class="flex items-center justify-center w-2/4 h-full mr-1 relative"
                                    @dragover="dragover" @drop="drop($event, 'f3_1')">
                                    <label for="dropzone1-file_f3"
                                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-bgddimg hover:bg-zinc-600/10"
                                        id="label_f3_1">
                                        <div class="flex flex-col items-center justify-center pt-4 pb-6 font-sans">
                                            <svg class="h-7 w-7 text-zinc-500" viewBox="0 0 24 24" fill="none"
                                                stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                                                <circle cx="12" cy="12" r="3" />
                                            </svg>
                                            <p class="mb-0 text-sm text-zinc-500">Open Both Eyes Image
                                            </p>
                                            <div class="flex justify-start">
                                                <p class="text-xs text-zinc-400">Drop your image here, or</p>
                                                <p class="text-xs text-zinc-400 underline ml-1">browse</p>
                                            </div>
                                        </div>
                                        <input accept="image/png, image/jpeg, image/jpg" id="dropzone1-file_f3" type="file"
                                            class="hidden" @change="onFile_($event, 'f3_1')" />
                                    </label>
                                    <img :src="image_f3_1" class="w-full h-64 border-2 border-dashed rounded-lg"
                                        id="img_f3_1" hidden />
                                    <div class="absolute right-3 top-2" id="btn_f3_1" hidden>
                                        <button type="button" @click="cancel('f3_1')">
                                            <svg class="h-5 w-5 text-red-700 hover:text-red-900" viewBox="0 0 24 24"
                                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <circle cx="12" cy="12" r="10" />
                                                <line x1="15" y1="9" x2="9" y2="15" />
                                                <line x1="9" y1="9" x2="15" y2="15" />
                                            </svg>
                                        </button>
                                    </div>
                                </div>

                                <div class="flex items-center justify-center w-2/4 h-full ml-1 relative"
                                    @dragover="dragover" @drop="drop($event, 'f3_2')">
                                    <label for="dropzone2-file_f3"
                                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-bgddimg hover:bg-zinc-600/10"
                                        id="label_f3_2">
                                        <div class="flex flex-col items-center justify-center pt-4 pb-6 font-sans">
                                            <img src="../image/close-eye.png" width="30px" alt="" srcset="">
                                            <p class="mb-0 text-sm text-zinc-500">Close Both Eyes Image
                                            </p>
                                            <div class="flex justify-start">
                                                <p class="text-xs text-zinc-400 ">Drop your image here, or</p>
                                                <p class="text-xs text-zinc-400 underline ml-1">browse</p>
                                            </div>
                                        </div>
                                        <input accept="image/png, image/jpeg, image/jpg" id="dropzone2-file_f3" type="file"
                                            class="hidden" @change="onFile_($event, 'f3_2')" />
                                    </label>
                                    <img :src="image_f3_2" class="w-full h-64 border-2 border-dashed rounded-lg"
                                        id="img_f3_2" hidden />
                                    <div class="absolute right-3 top-2" id="btn_f3_2" hidden>
                                        <button type="button" @click="cancel('f3_2')">
                                            <svg class="h-5 w-5 text-red-700 hover:text-red-900" viewBox="0 0 24 24"
                                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <circle cx="12" cy="12" r="10" />
                                                <line x1="15" y1="9" x2="9" y2="15" />
                                                <line x1="9" y1="9" x2="15" y2="15" />
                                            </svg>
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <p class="flex justify-end text-xxs text-zinc-500 font-sans mt-2">Page 4</p>
                        </div>

                    </div>
                    <button type="button"
                        class="w-20 ml-auto flex items-center h-full hover:bg-[#B2AAAA] active:bg-[#B2AAAA] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                        @click="next">
                        <div class="ml-auto mr-auto">
                            <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="9 18 15 12 9 6" />
                            </svg>
                        </div>
                    </button>
                </div>

                <!-- 5 -->
                <div class="w-120 bg-[bginput] rounded-lg flex" style="height: 25rem;" id="f_4" hidden>
                    <button type="button"
                        class="w-20 mr-auto flex items-center h-full hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                        @click="back">
                        <div class="ml-auto mr-auto">
                            <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="15 18 9 12 15 6" />
                            </svg>
                        </div>
                    </button>
                    <div class="w-8/12 h-80 mr-auto ml-auto mt-3 bg-white rounded-lg shadow-md">
                        <div class="text-left ml-10 mr-10 mt-4">
                            <div
                                class="flex flex-row items-center border-b border-zinc-400 py-0 w-44 hover:border-zinc-500">
                                <input
                                    class="pb-1 block appearance-none bg-transparent border-none w-full text-gray-700 font-sans font-medium mr-3 py-0 px-2 leading-tight focus:outline-none"
                                    type="text" placeholder="Follow up period" id="text_follow_0" v-model="text_follow_5"
                                    oninput="javascript: if (text_follow_5.length > this.maxLength) text_follow_5 = text_follow_5.slice(0, this.maxLength);"
                                    maxlength="14" aria-label="Follow up" @change="input_follow">
                                <svg class="h-6 w-6 text-zinc-400 hover:text-zinc-500" fill="none" viewBox="0 0 24 24"
                                    stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                                </svg>
                            </div>
                            <div class="flex text-xxs text-text1 text-zinc-400 font-sans mt-1"
                                :style="{ color: text_follow_5.length == 14 ? 'red' : 'gray' }">Please input your
                                following up
                                period above
                                within
                                <div class="flex flex-row ml-1 mr-1 input-group-addon" v-text="(14 - text_follow_5.length)"
                                    :style="{ color: text_follow_5.length == 14 ? 'red' : 'gray' }"></div>characters
                            </div>
                            <div class="flex h-full mt-2">
                                <div class="flex items-center justify-center w-2/4 h-full mr-1 relative"
                                    @dragover="dragover" @drop="drop($event, 'f4_1')">
                                    <label for="dropzone1-file_f4"
                                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-bgddimg hover:bg-zinc-600/10"
                                        id="label_f4_1">
                                        <div class="flex flex-col items-center justify-center pt-4 pb-6 font-sans">
                                            <svg class="h-7 w-7 text-zinc-500" viewBox="0 0 24 24" fill="none"
                                                stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                                                <circle cx="12" cy="12" r="3" />
                                            </svg>
                                            <p class="mb-0 text-sm text-zinc-500">Open Both Eyes Image
                                            </p>
                                            <div class="flex justify-start">
                                                <p class="text-xs text-zinc-400">Drop your image here, or</p>
                                                <p class="text-xs text-zinc-400 underline ml-1">browse</p>
                                            </div>
                                        </div>
                                        <input accept="image/png, image/jpeg, image/jpg" id="dropzone1-file_f4" type="file"
                                            class="hidden" @change="onFile_($event, 'f4_1')" />
                                    </label>
                                    <img :src="image_f4_1" class="w-full h-64 border-2 border-dashed rounded-lg"
                                        id="img_f4_1" hidden />
                                    <div class="absolute right-3 top-2" id="btn_f4_1" hidden>
                                        <button type="button" @click="cancel('f4_1')">
                                            <svg class="h-5 w-5 text-red-700 hover:text-red-900" viewBox="0 0 24 24"
                                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <circle cx="12" cy="12" r="10" />
                                                <line x1="15" y1="9" x2="9" y2="15" />
                                                <line x1="9" y1="9" x2="15" y2="15" />
                                            </svg>
                                        </button>
                                    </div>
                                </div>

                                <div class="flex items-center justify-center w-2/4 h-full ml-1 relative"
                                    @dragover="dragover" @drop="drop($event, 'f4_2')">
                                    <label for="dropzone2-file_f4"
                                        class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-bgddimg hover:bg-zinc-600/10"
                                        id="label_f4_2">
                                        <div class="flex flex-col items-center justify-center pt-4 pb-6 font-sans">
                                            <img src="../image/close-eye.png" width="30px" alt="" srcset="">
                                            <p class="mb-0 text-sm text-zinc-500">Close Both Eyes Image
                                            </p>
                                            <div class="flex justify-start">
                                                <p class="text-xs text-zinc-400 ">Drop your image here, or</p>
                                                <p class="text-xs text-zinc-400 underline ml-1">browse</p>
                                            </div>
                                        </div>
                                        <input accept="image/png, image/jpeg, image/jpg" id="dropzone2-file_f4" type="file"
                                            class="hidden" @change="onFile_($event, 'f4_2')" />
                                    </label>
                                    <img :src="image_f4_2" class="w-full h-64 border-2 border-dashed rounded-lg"
                                        id="img_f4_2" hidden />
                                    <div class="absolute right-3 top-2" id="btn_f4_2" hidden>
                                        <button type="button" @click="cancel('f4_2')">
                                            <svg class="h-5 w-5 text-red-700 hover:text-red-900" viewBox="0 0 24 24"
                                                fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                                stroke-linejoin="round">
                                                <circle cx="12" cy="12" r="10" />
                                                <line x1="15" y1="9" x2="9" y2="15" />
                                                <line x1="9" y1="9" x2="15" y2="15" />
                                            </svg>
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <p class="flex justify-end text-xxs text-zinc-500 font-sans mt-2">Page 5</p>
                        </div>

                    </div>
                    <div
                        class="w-20 ml-auto flex items-center h-full hover:bg-[#B2AAAA] active:bg-[#B2AAAA] focus:outline-none focus:ring focus:bg-[#ded2d2]">
                        <div class="ml-auto mr-auto">

                        </div>
                    </div>
                </div>


            </form>
        </div>

        <div class="container mb-2 w-full mx-auto px-40 pt-4 pb-2" id="div_des" hidden>
            <div class="overflow-x-scroll rounded-lg bg-[#D9D9D9] px-2 py-2">
                <table>
                    <thead>
                        <tr>
                            <th class="me-2 rounded-lg w-40">
                                <div class="me-2 rounded-lg bg-[#5A528D] p-3">
                                    <img src="../image/combine.svg" width="20px" class="ml-auto mr-auto" alt="" srcset="">
                                </div>
                            </th>
                            <th class="me-2 rounded-lg w-40" id="des0_0" hidden>
                                <div class="text-text1 font-sans text-sm font-medium me-2 w-40 rounded-lg bg-[#F2F2F2] p-3">
                                    <p id="text_follow_1"></p>
                                </div>
                            </th>
                            <th class="me-2 rounded-lg w-40" id="des0_1" hidden>
                                <div class="text-text1 font-sans text-sm font-medium me-2 w-40 rounded-lg bg-[#F2F2F2] p-3">
                                    <p id="text_follow_2"></p>
                                </div>
                            </th>
                            <th class="me-2 rounded-lg w-40" id="des0_2" hidden>
                                <div class="text-text1 font-sans text-sm font-medium me-2 w-40 rounded-lg bg-[#F2F2F2] p-3">
                                    <p id="text_follow_3"></p>
                                </div>
                            </th>
                            <th class="me-2 rounded-lg w-40" id="des0_3" hidden>
                                <div class="text-text1 font-sans text-sm font-medium me-2 w-40 rounded-lg bg-[#F2F2F2] p-3">
                                    <p id="text_follow_4"></p>
                                </div>
                            </th>
                            <th class="me-2 rounded-lg w-40" id="des0_4" hidden>
                                <div class="text-text1 font-sans text-sm font-medium me-2 w-40 rounded-lg bg-[#F2F2F2] p-3">
                                    <p id="text_follow_5"></p>
                                </div>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr id="des1_0" hidden>
                            <th>
                                <div
                                    class="w-40 me-2 mt-2 rounded-lg text-sm text-text1 font-sans font-medium bg-[#F2F2F2] p-3">
                                    <p id="text_follow_1_1"></p>
                                </div>
                            </th>
                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_1"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-transparent"
                                        aria-label="Default select example">
                                        <option value="Open, Close" selected>Open, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>
                        </tr>
                        <tr id="des1_1" hidden>
                            <th>
                                <div
                                    class="w-40 me-2 mt-2 rounded-lg text-sm text-text1 font-sans font-medium bg-[#F2F2F2] p-3">
                                    <p id="text_follow_2_2"></p>
                                </div>
                            </th>
                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_2"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Open" selected>Open, Open</option>
                                        <option value="Open, Close">Open, Close</option>
                                        <option value="Close, Close">Close, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>
                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_3"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Close" selected>Open, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>
                        </tr>

                        <tr id="des1_2" hidden>
                            <th>
                                <div
                                    class="w-40 me-2 mt-2 rounded-lg text-sm text-text1 font-sans font-medium bg-[#F2F2F2] p-3">
                                    <p id="text_follow_3_3"></p>
                                </div>
                            </th>
                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_4"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Open" selected>Open, Open</option>
                                        <option value="Open, Close">Open, Close</option>
                                        <option value="Close, Close">Close, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>
                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_5"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Open" selected>Open, Open</option>
                                        <option value="Open, Close">Open, Close</option>
                                        <option value="Close, Close">Close, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>
                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_6"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Close" selected>Open, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>
                        </tr>

                        <tr id="des1_3" hidden>
                            <th>
                                <div
                                    class="w-40 me-2 mt-2 rounded-lg text-sm text-text1 font-sans font-medium bg-[#F2F2F2] p-3">
                                    <p id="text_follow_4_4"></p>
                                </div>
                            </th>
                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_7"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Open" selected>Open, Open</option>
                                        <option value="Open, Close">Open, Close</option>
                                        <option value="Close, Close">Close, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>

                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_8"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Open" selected>Open, Open</option>
                                        <option value="Open, Close">Open, Close</option>
                                        <option value="Close, Close">Close, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>

                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_9"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Open" selected>Open, Open</option>
                                        <option value="Open, Close">Open, Close</option>
                                        <option value="Close, Close">Close, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>
                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_10"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Close" selected>Open, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>
                        </tr>


                        <tr id="des1_4" hidden>
                            <th>
                                <div
                                    class="w-40 me-2 mt-2 rounded-lg text-sm text-text1 font-sans font-medium bg-[#F2F2F2] p-3">
                                    <p id="text_follow_5_5"></p>
                                </div>
                            </th>
                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_11"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Open" selected>Open, Open</option>
                                        <option value="Open, Close">Open, Close</option>
                                        <option value="Close, Close">Close, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>

                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_12"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Open" selected>Open, Open</option>
                                        <option value="Open, Close">Open, Close</option>
                                        <option value="Close, Close">Close, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>

                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_13"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Open" selected>Open, Open</option>
                                        <option value="Open, Close">Open, Close</option>
                                        <option value="Close, Close">Close, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>

                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_14"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Open" selected>Open, Open</option>
                                        <option value="Open, Close">Open, Close</option>
                                        <option value="Close, Close">Close, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>

                            <td class="rounded-lg">
                                <div class="text-dark p-2.5 mt-1 me-2 w-40 bg-white rounded-lg">
                                    <select id="select_15"
                                        class="form-select appearance-noneblockw-fullpx-3 py-1.5text-basefont-normal text-text1 font-sans text-sm font-normal bg-white bg-clip-padding bg-no-repeatborder border-none roundedtransitionease-in-out m-0
                                                                                                                                                focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
                                        aria-label="Default select example">
                                        <option value="Open, Close" selected>Open, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>
                        </tr>


                    </tbody>
                </table>


            </div>


        </div>


        <div id="div_img" hidden>
            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img1">
                <div class="w-20 ml-auto flex items-center h-full">
                    <div class="ml-auto mr-auto">

                    </div>
                </div>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_0"></h1>
                            <h1 id="status1_0" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor0" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_0" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor0_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img2" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_1"></h1>
                            <h1 id="status1_1" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor1" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_1" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor1_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img3" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_2"></h1>
                            <h1 id="status1_2" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor2" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_2" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor2_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img4" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_3"></h1>
                            <h1 id="status1_3" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor3" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_3" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor3_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img5" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_4"></h1>
                            <h1 id="status1_4" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor4" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_4" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor4_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img6" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_5"></h1>
                            <h1 id="status1_5" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor5" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_5" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor5_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img7" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_6"></h1>
                            <h1 id="status1_6" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor6" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_6" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor6_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img8" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_7"></h1>
                            <h1 id="status1_7" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor7" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_7" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor7_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img9" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_8"></h1>
                            <h1 id="status1_8" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor8" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_8" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor8_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img10" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_9"></h1>
                            <h1 id="status1_9" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor9" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_9" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor9_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img11" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_10"></h1>
                            <h1 id="status1_10" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor10" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_10" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor10_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img12" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_11"></h1>
                            <h1 id="status1_11" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor11" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_11" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor11_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img13" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_12"></h1>
                            <h1 id="status1_12" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor12" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_12" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor12_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img14" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_13"></h1>
                            <h1 id="status1_13" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor13" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_13" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor13_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img15" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-8/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div class="text-left ml-20 mr-20 mt-5">
                        <div class="flex">
                            <h1 id="name_14"></h1>
                            <h1 id="status1_14" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor14" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="status2_14" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor14_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_img">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>




        </div>

        <div id="link" hidden>

        </div>



        <div>
            <button id="btn_main_next" type="button" @click="next_submit"
                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Next
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 ml-2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M12.75 15l3-3m0 0l-3-3m3 3h-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>

            </button>

            <button id="btn_des_next1" type="button" @click="back_to_main"
                class="me-2 inline-flex items-center bg-bg hover:bg-btn33 text-btn1 border-1 border-btn1 py-2.2 px-14 focus:outline-none rounded-lg text-lg"
                hidden>Back<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 ml-2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M11.25 9l-3 3m0 0l3 3m-3-3h7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
            </button>

            <button id="btn_des_next2" type="button" @click="submit"
                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg"
                hidden>Submit
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 ml-2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M12.75 15l3-3m0 0l-3-3m3 3h-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>

            </button>


            <button id="btn_img_back" type="button" @click="back_to_des"
                class="me-2 inline-flex items-center bg-bg hover:bg-btn33 text-btn1 border-1 border-btn1 py-2.2 px-14 focus:outline-none rounded-lg text-lg"
                hidden>Back<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 ml-2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M11.25 9l-3 3m0 0l3 3m-3-3h7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
            </button>

            <button hidden id="btn_img_load" type="button" @click="load_img"
                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">load
                image
            </button>

        </div>

    </div>
</template>

<style>
.cheapest {
    z-index: 85;
    opacity: .3;
}
</style>


<script>
import axios from 'axios'
import 'tui-color-picker/dist/tui-color-picker.css';
import 'tui-image-editor/dist/tui-image-editor.css';
import { ImageEditor } from '@toast-ui/vue-image-editor';

export default {
    name: "TextContent",
    components: {
        'tui-image-editor': ImageEditor,
    },
    data() {
        return {
            current: 1,
            image_f0_1: null,
            image_f0_2: null,
            files_f0_1: null,
            files_f0_2: null,
            image_f1_1: null,
            image_f1_2: null,
            files_f1_1: null,
            files_f1_2: null,
            image_f2_1: null,
            image_f2_2: null,
            files_f2_1: null,
            files_f2_2: null,
            image_f3_1: null,
            image_f3_2: null,
            files_f3_1: null,
            files_f3_2: null,
            image_f4_1: null,
            image_f4_2: null,
            files_f4_1: null,
            files_f4_2: null,

            text_follow_1: "",
            text_follow_2: "",
            text_follow_3: "",
            text_follow_4: "",
            text_follow_5: "",

            image_count: 0,
            image_end: 0,
            haveImg: false,
            filelist: [], // Store our uploaded files,
            useDefaultUI: true,
            options: {
                includeUI: {
                    menuBarPosition: 'bottom'
                },
                cssMaxWidth: 700,
                cssMaxHeight: 1000,

            },
        }
    },
    methods: {
        createImage(file) {
            if (!file.type.match('image/(png|jpeg|jpg)')) {
                alert('Please choose a new image again because the file is invalid. Only JPG, JPEG, and PNG files are allowed.');
                return;
            }
            this.haveImg = true;
            var reader = new FileReader();
            reader.onload = (e) => {
                this.image = e.target.result;
            };
            reader.readAsDataURL(file);
        },
        remove(i) {
            this.filelist.splice(i, 1);
        },
        dragover(event) {
            event.preventDefault();
        },
        cancel(item) {
            if (item === 'f0_1') {
                document.getElementById("label_f0_1").hidden = false;
                document.getElementById("img_f0_1").hidden = true;
                document.getElementById("btn_f0_1").hidden = true;
                this.image_f0_1 = null;
                this.files_f0_1 = null;
            } else if (item === 'f0_2') {
                document.getElementById("label_f0_2").hidden = false;
                document.getElementById("img_f0_2").hidden = true;
                document.getElementById("btn_f0_2").hidden = true;
                this.image_f0_2 = null;
                this.files_f0_2 = null;
            } else if (item === 'f1_1') {
                document.getElementById("label_f1_1").hidden = false;
                document.getElementById("img_f1_1").hidden = true;
                document.getElementById("btn_f1_1").hidden = true;
                this.image_f1_1 = null;
                this.files_f1_1 = null;
            } else if (item === 'f1_2') {
                document.getElementById("label_f1_2").hidden = false;
                document.getElementById("img_f1_2").hidden = true;
                document.getElementById("btn_f1_2").hidden = true;
                this.image_f1_2 = null;
                this.files_f1_2 = null;
            } else if (item === 'f2_1') {
                document.getElementById("label_f2_1").hidden = false;
                document.getElementById("img_f2_1").hidden = true;
                document.getElementById("btn_f2_1").hidden = true;
                this.image_f2_1 = null;
                this.files_f2_1 = null;
            } else if (item === 'f2_2') {
                document.getElementById("label_f2_2").hidden = false;
                document.getElementById("img_f2_2").hidden = true;
                document.getElementById("btn_f2_2").hidden = true;
                this.image_f2_2 = null;
                this.files_f2_2 = null;
            } else if (item === 'f3_1') {
                document.getElementById("label_f3_1").hidden = false;
                document.getElementById("img_f3_1").hidden = true;
                document.getElementById("btn_f3_1").hidden = true;
                this.image_f3_1 = null;
                this.files_f3_1 = null;
            } else if (item === 'f4_1') {
                document.getElementById("label_f4_1").hidden = false;
                document.getElementById("img_f4_1").hidden = true;
                document.getElementById("btn_f4_1").hidden = true;
                this.image_f4_1 = null;
                this.files_f4_1 = null;
            } else if (item === 'f4_2') {
                document.getElementById("label_f4_2").hidden = false;
                document.getElementById("img_f4_2").hidden = true;
                document.getElementById("btn_f4_2").hidden = true;
                this.image_f4_2 = null;
                this.files_f4_2 = null;
            }
        },
        drop(event, item) {
            event.preventDefault();
            console.log(item);
            if (item === 'f0_1') {
                const files = event.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0]);
                this.image_f0_1 = URL.createObjectURL(files[0]);
                document.getElementById("label_f0_1").hidden = true;
                document.getElementById("img_f0_1").hidden = false;
                document.getElementById("btn_f0_1").hidden = false;
                this.files_f0_1 = files[0];
                document.getElementById("img_f0_1").src = this.image_f0_1;
                console.log(files);
            } else if (item === 'f0_2') {
                const files = event.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0]);
                this.image_f0_2 = URL.createObjectURL(files[0]);
                document.getElementById("label_f0_2").hidden = true;
                document.getElementById("img_f0_2").hidden = false;
                document.getElementById("btn_f0_2").hidden = false;
                this.files_f0_2 = files[0];
                document.getElementById("img_f0_2").src = this.image_f0_2;
            } else if (item === 'f1_1') {
                const files = event.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0]);
                this.image_f1_1 = URL.createObjectURL(files[0]);
                document.getElementById("label_f1_1").hidden = true;
                document.getElementById("img_f1_1").hidden = false;
                document.getElementById("btn_f1_1").hidden = false;
                this.files_f1_1 = files[0];
                document.getElementById("img_f1_1").src = this.image_f1_1;
            } else if (item === 'f1_2') {
                const files = event.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0]);
                this.image_f1_2 = URL.createObjectURL(files[0]);
                document.getElementById("label_f1_2").hidden = true;
                document.getElementById("img_f1_2").hidden = false;
                document.getElementById("btn_f1_2").hidden = false;
                this.files_f1_2 = files[0];
                document.getElementById("img_f1_2").src = this.image_f1_2;
            } else if (item === 'f2_1') {
                const files = event.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0]);
                this.image_f2_1 = URL.createObjectURL(files[0]);
                document.getElementById("label_f2_1").hidden = true;
                document.getElementById("img_f2_1").hidden = false;
                document.getElementById("btn_f2_1").hidden = false;
                this.files_f2_1 = files[0];
                document.getElementById("img_f2_1").src = this.image_f2_1;
            } else if (item === 'f2_2') {
                const files = event.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0]);
                this.image_f2_2 = URL.createObjectURL(files[0]);
                document.getElementById("label_f2_2").hidden = true;
                document.getElementById("img_f2_2").hidden = false;
                document.getElementById("btn_f2_2").hidden = false;
                this.files_f2_2 = files[0];
                document.getElementById("img_f2_2").src = this.image_f2_2;
            } else if (item === 'f3_1') {
                const files = event.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0]);
                this.image_f3_1 = URL.createObjectURL(files[0]);
                document.getElementById("label_f3_1").hidden = true;
                document.getElementById("img_f3_1").hidden = false;
                document.getElementById("btn_f3_1").hidden = false;
                this.files_f3_1 = files[0];
                document.getElementById("img_f3_1").src = this.image_f3_1;
            } else if (item === 'f3_2') {
                const files = event.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0]);
                this.image_f3_2 = URL.createObjectURL(files[0]);
                document.getElementById("label_f3_2").hidden = true;
                document.getElementById("img_f3_2").hidden = false;
                document.getElementById("btn_f3_2").hidden = false;
                this.files_f3_2 = files[0];
                document.getElementById("img_f3_2").src = this.image_f3_2;
            } else if (item === 'f4_1') {
                const files = event.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0]);
                this.image_f4_1 = URL.createObjectURL(files[0]);
                document.getElementById("label_f4_1").hidden = true;
                document.getElementById("img_f4_1").hidden = false;
                document.getElementById("btn_f4_1").hidden = false;
                this.files_f4_1 = files[0];
                document.getElementById("img_f4_1").src = this.image_f4_1;
            } else if (item === 'f4_2') {
                const files = event.dataTransfer.files
                if (!files.length) return
                this.createImage(files[0]);
                this.image_f4_2 = URL.createObjectURL(files[0]);
                document.getElementById("label_f4_2").hidden = true;
                document.getElementById("img_f4_2").hidden = false;
                document.getElementById("btn_f4_2").hidden = false;
                this.files_f4_2 = files[0];
                document.getElementById("img_f4_2").src = this.image_f4_2;
            }
        },
        back() {
            if (this.current == 2) {
                document.getElementById("f_1").hidden = true;
                document.getElementById("f_0").hidden = false;
                this.current = 1;
            } else if (this.current == 3) {
                document.getElementById("f_2").hidden = true;
                document.getElementById("f_1").hidden = false;
                this.current = 2;
            } else if (this.current == 4) {
                document.getElementById("f_3").hidden = true;
                document.getElementById("f_2").hidden = false;
                this.current = 3;
            } else if (this.current == 5) {
                document.getElementById("f_4").hidden = true;
                document.getElementById("f_3").hidden = false;
                this.current = 4;
            }

        },
        next() {
            if (this.current == 1) {
                if (this.text_follow_1 == '' || this.image_f0_1 == null || this.image_f0_2 == null) {
                    alert('Please fill in all the required information');
                    return;
                }
                document.getElementById("f_0").hidden = true;
                document.getElementById("f_1").hidden = false;
                this.current = 2;
            } else if (this.current == 2) {
                if (this.text_follow_2 == '' || this.image_f1_1 == null || this.image_f1_2 == null) {
                    alert('Please fill in all the required information');
                    return;
                }
                document.getElementById("f_1").hidden = true;
                document.getElementById("f_2").hidden = false;
                this.current = 3;
            } else if (this.current == 3) {
                if (this.text_follow_3 == '' || this.image_f2_1 == null || this.image_f2_2 == null) {
                    alert('Please fill in all the required information');
                    return;
                }

                document.getElementById("f_2").hidden = true;
                document.getElementById("f_3").hidden = false;
                this.current = 4;
            } else if (this.current == 4) {
                if (this.text_follow_4 == '' || this.image_f3_1 == null || this.image_f3_2 == null) {
                    alert('Please fill in all the required information');
                    return;
                }
                document.getElementById("f_3").hidden = true;
                document.getElementById("f_4").hidden = false;
                this.current = 5;
            }
        },
        input_follow(e) {
            if (this.current == 1) {
                this.text_follow_1 = e.target.value;
                if (this.text_follow_1.length > 0) {
                    document.getElementById("des0_0").hidden = false;
                    document.getElementById("des1_0").hidden = false;
                    document.getElementById("text_follow_1").innerText = this.text_follow_1;
                    document.getElementById("text_follow_1_1").innerText = this.text_follow_1;
                } else {
                    document.getElementById("des1_0").hidden = true;
                    document.getElementById("des0_0").hidden = true;
                }
            } else if (this.current == 2) {
                this.text_follow_2 = e.target.value;
                if (this.text_follow_2.length > 0) {
                    document.getElementById("des0_1").hidden = false;
                    document.getElementById("des1_1").hidden = false;
                    document.getElementById("text_follow_2").innerText = this.text_follow_2;
                    document.getElementById("text_follow_2_2").innerText = this.text_follow_2;
                } else {
                    document.getElementById("des1_1").hidden = true;
                    document.getElementById("des0_1").hidden = true;
                }
            } else if (this.current == 3) {
                this.text_follow_3 = e.target.value
                if (this.text_follow_3.length > 0) {
                    document.getElementById("des0_2").hidden = false;
                    document.getElementById("des1_2").hidden = false;
                    document.getElementById("text_follow_3").innerText = this.text_follow_3;
                    document.getElementById("text_follow_3_3").innerText = this.text_follow_3;
                } else {
                    document.getElementById("des1_2").hidden = true;
                    document.getElementById("des0_2").hidden = true;
                }
            } else if (this.current == 4) {
                this.text_follow_4 = e.target.value;
                if (this.text_follow_4.length > 0) {
                    document.getElementById("des0_3").hidden = false;
                    document.getElementById("des1_3").hidden = false;
                    document.getElementById("text_follow_4").innerText = this.text_follow_4;
                    document.getElementById("text_follow_4_4").innerText = this.text_follow_4;
                } else {
                    document.getElementById("des1_3").hidden = true;
                    document.getElementById("des0_3").hidden = true;
                }
            } else if (this.current == 5) {
                this.text_follow_5 = e.target.value;
                if (this.text_follow_5.length > 0) {
                    document.getElementById("des0_4").hidden = false;
                    document.getElementById("des1_4").hidden = false;
                    document.getElementById("text_follow_5").innerText = this.text_follow_5;
                    document.getElementById("text_follow_5_5").innerText = this.text_follow_5;
                } else {
                    document.getElementById("des1_4").hidden = true;
                    document.getElementById("des0_4").hidden = true;
                }
            }
        },
        onFile_(e, i) {
            e.preventDefault();
            const files = e.target.files
            if (!files.length) return
            if (i === 'f0_1') {
                this.image_f0_1 = URL.createObjectURL(files[0]);
                document.getElementById("label_f0_1").hidden = true;
                document.getElementById("img_f0_1").hidden = false;
                document.getElementById("btn_f0_1").hidden = false;
                this.files_f0_1 = files[0];
                document.getElementById("img_f0_1").src = this.image_f0_1;
            } else if (i === 'f0_2') {
                this.image_f0_2 = URL.createObjectURL(files[0]);
                document.getElementById("label_f0_2").hidden = true;
                document.getElementById("img_f0_2").hidden = false;
                document.getElementById("btn_f0_2").hidden = false;
                this.files_f0_2 = files[0];
                document.getElementById("img_f0_2").src = this.image_f0_2;
            } else if (i === 'f1_1') {
                this.image_f1_1 = URL.createObjectURL(files[0]);
                document.getElementById("label_f1_1").hidden = true;
                document.getElementById("img_f1_1").hidden = false;
                document.getElementById("btn_f1_1").hidden = false;
                this.files_f1_1 = files[0];
                document.getElementById("img_f1_1").src = this.image_f1_1;
            } else if (i === 'f1_2') {
                this.image_f1_2 = URL.createObjectURL(files[0]);
                document.getElementById("label_f1_2").hidden = true;
                document.getElementById("img_f1_2").hidden = false;
                document.getElementById("btn_f1_2").hidden = false;
                this.files_f1_2 = files[0];
                document.getElementById("img_f1_2").src = this.image_f1_2;
            } else if (i === 'f2_1') {
                this.image_f2_1 = URL.createObjectURL(files[0]);
                document.getElementById("label_f2_1").hidden = true;
                document.getElementById("img_f2_1").hidden = false;
                document.getElementById("btn_f2_1").hidden = false;
                this.files_f2_1 = files[0];
                document.getElementById("img_f2_1").src = this.image_f2_1;
            } else if (i === 'f2_2') {
                this.image_f2_2 = URL.createObjectURL(files[0]);
                document.getElementById("label_f2_2").hidden = true;
                document.getElementById("img_f2_2").hidden = false;
                document.getElementById("btn_f2_2").hidden = false;
                this.files_f2_2 = files[0];
                document.getElementById("img_f2_2").src = this.image_f2_2;
            } else if (i === 'f3_1') {
                this.image_f3_1 = URL.createObjectURL(files[0]);
                document.getElementById("label_f3_1").hidden = true;
                document.getElementById("img_f3_1").hidden = false;
                document.getElementById("btn_f3_1").hidden = false;
                this.files_f3_1 = files[0];
                document.getElementById("img_f3_1").src = this.image_f3_1;
            } else if (i === 'f3_2') {
                this.image_f3_2 = URL.createObjectURL(files[0]);
                document.getElementById("label_f3_2").hidden = true;
                document.getElementById("img_f3_2").hidden = false;
                document.getElementById("btn_f3_2").hidden = false;
                this.files_f3_2 = files[0];
                document.getElementById("img_f3_2").src = this.image_f3_2;
            } else if (i === 'f4_1') {
                this.image_f4_1 = URL.createObjectURL(files[0]);
                document.getElementById("label_f4_1").hidden = true;
                document.getElementById("img_f4_1").hidden = false;
                document.getElementById("btn_f4_1").hidden = false;
                this.files_f4_1 = files[0];
                document.getElementById("img_f4_1").src = this.image_f4_1;
            } else if (i === 'f4_2') {
                this.image_f4_2 = URL.createObjectURL(files[0]);
                document.getElementById("label_f4_2").hidden = true;
                document.getElementById("img_f4_2").hidden = false;
                document.getElementById("btn_f4_2").hidden = false;
                this.files_f4_2 = files[0];
                document.getElementById("img_f4_2").src = this.image_f4_2;
            }
        },
        next_submit() {
            if (this.current == 1) {
                if (this.text_follow_1 == '' || this.image_f0_1 == null || this.image_f0_2 == null) {
                    alert('Please enter the information before clicking the next button');
                    return;
                }
            }
            document.getElementById("main").hidden = true;
            document.getElementById("div_des").hidden = false;
            document.getElementById("div_main").hidden = true;
            document.getElementById("des").hidden = false;
            document.getElementById("btn_main_next").hidden = true;
            document.getElementById("btn_des_next1").hidden = false;
            document.getElementById("btn_des_next2").hidden = false;


        },
        back_to_main() {
            document.getElementById("main").hidden = false;
            document.getElementById("div_des").hidden = true;
            document.getElementById("div_main").hidden = false;
            document.getElementById("des").hidden = true;
            document.getElementById("btn_main_next").hidden = false;
            document.getElementById("btn_des_next1").hidden = true;
            document.getElementById("btn_des_next2").hidden = true;
        },
        back_to_des() {
            document.getElementById("div_des").hidden = false;
            document.getElementById("btn_des_next1").hidden = false;
            document.getElementById("btn_des_next2").hidden = false;
            document.getElementById("des").hidden = false;
            document.getElementById("div_img").hidden = true;
            document.getElementById("btn_img_back").hidden = true;
            document.getElementById("btn_img_load").hidden = true;
            this.image_count = 0;
        },
        submit() {
            let formData = new FormData();

            let files_1_2 = document.getElementById("select_1").value;

            let files_3_1 = document.getElementById("select_2").value;
            let files_3_2 = document.getElementById("select_3").value;

            let files_4_1 = document.getElementById("select_4").value;
            let files_4_2 = document.getElementById("select_5").value;
            let files_4_3 = document.getElementById("select_6").value;

            let files_5_1 = document.getElementById("select_7").value;
            let files_5_2 = document.getElementById("select_8").value;
            let files_5_3 = document.getElementById("select_9").value;
            let files_5_4 = document.getElementById("select_10").value;

            let files_6_1 = document.getElementById("select_11").value;
            let files_6_2 = document.getElementById("select_12").value;
            let files_6_3 = document.getElementById("select_13").value;
            let files_6_4 = document.getElementById("select_14").value;
            let files_6_5 = document.getElementById("select_15").value;

            formData.append('files', this.files_f0_1);
            formData.append('files', this.files_f0_2);

            formData.append('files', this.files_f1_1);
            formData.append('files', this.files_f1_2);

            formData.append('files', this.files_f2_1);
            formData.append('files', this.files_f2_2);

            formData.append('files', this.files_f3_1);
            formData.append('files', this.files_f3_2);

            formData.append('files', this.files_f4_1);
            formData.append('files', this.files_f4_2);

            formData.append('files', this.files_f5_1);
            formData.append('files', this.files_f5_2);


            formData.append("files 1-2", files_1_2);
            formData.append("files 3-1", files_3_1);
            formData.append("files 3-2", files_3_2);
            formData.append("files 4-1", files_4_1);
            formData.append("files 4-2", files_4_2);
            formData.append("files 4-3", files_4_3);
            formData.append("files 5-1", files_5_1);
            formData.append("files 5-2", files_5_2);
            formData.append("files 5-3", files_5_3);
            formData.append("files 5-4", files_5_4);
            formData.append("files 6-1", files_6_1);
            formData.append("files 6-2", files_6_2);
            formData.append("files 6-3", files_6_3);
            formData.append("files 6-4", files_6_4);
            formData.append("files 6-5", files_6_5);


            formData.append("type 1-2", `${this.text_follow_1}`);
            formData.append("type 3-1", `${this.text_follow_2} and ${this.text_follow_1}`);
            formData.append("type 3-2", `${this.text_follow_2}`);
            formData.append("type 4-1", `${this.text_follow_3} and ${this.text_follow_1}`);
            formData.append("type 4-2", `${this.text_follow_3} and ${this.text_follow_2}`);
            formData.append("type 4-3", `${this.text_follow_3}`);
            formData.append("type 5-1", `${this.text_follow_4} and ${this.text_follow_1}`);
            formData.append("type 5-2", `${this.text_follow_4} and ${this.text_follow_2}`);
            formData.append("type 5-3", `${this.text_follow_4} and ${this.text_follow_3}`);
            formData.append("type 5-4", `${this.text_follow_4}`);
            formData.append("type 6-1", `${this.text_follow_5} and ${this.text_follow_1}`);
            formData.append("type 6-2", `${this.text_follow_5} and ${this.text_follow_2}`);
            formData.append("type 6-3", `${this.text_follow_5} and ${this.text_follow_3}`);
            formData.append("type 6-4", `${this.text_follow_5} and ${this.text_follow_4}`);
            formData.append("type 6-5", `${this.text_follow_5}`);


            var html = "";
            axios.post('http://127.0.0.1:5000/upload_files',
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }
            ).then(function (response) {
                document.getElementById("div_des").hidden = true;
                document.getElementById("des").hidden = true;
                document.getElementById("btn_des_next1").hidden = true;
                document.getElementById("btn_des_next2").hidden = true;
                document.getElementById("div_img").hidden = false;
                document.getElementById("btn_img_load").hidden = false;
                document.getElementById("btn_img_back").hidden = false;


                let data = response.data;
                let objectLenght = Object.keys(data).length;
                for (let i = 0; i < objectLenght; i++) {
                    html = `${data[i].name}`;
                    document.getElementById(`name_${i}`).innerText = html;
                    html = `(R1) EBH: ${data[i][0][0]} px OSA: ${data[i][0][1]} px  (L1) EBH: ${data[i][0][2]} px OSA: ${data[i][0][3]} px`;
                    document.getElementById(`status1_${i}`).innerText = html;
                    html = `(R2) EBH: ${data[i][1][0]} px OSA: ${data[i][1][1]} px  (L2) EBH: ${data[i][1][2]} px OSA: ${data[i][1][3]} px`;
                    document.getElementById(`status2_${i}`).innerText = html;

                    document.getElementById('link').innerHTML += `<input type='text' id='url_image' value='${data[i].url1}'>`;
                    document.getElementById('link').innerHTML += `<input type='text' id='url_image' value='${data[i].url2}'>`;

                }


            })
                .catch(function (error) {
                    console.log('FAILURE!!');
                    console.log(error);
                });


        },
        next_img() {
            let link = document.querySelectorAll("[id='url_image']");

            let objectLenght = Object.keys(link).length;
            if (this.image_count != objectLenght / 2 - 1) {
                if (this.image_count === 0) {
                    document.getElementById("img1").hidden = true;
                    document.getElementById("img2").hidden = false;
                    this.image_count = 1;
                } else if (this.image_count === 1) {
                    document.getElementById("img2").hidden = true;
                    document.getElementById("img3").hidden = false;
                    this.image_count = 2;
                } else if (this.image_count === 2) {
                    document.getElementById("img3").hidden = true;
                    document.getElementById("img4").hidden = false;
                    this.image_count = 3;
                } else if (this.image_count === 3) {
                    document.getElementById("img4").hidden = true;
                    document.getElementById("img5").hidden = false;
                    this.image_count = 4;
                } else if (this.image_count === 4) {
                    document.getElementById("img5").hidden = true;
                    document.getElementById("img6").hidden = false;
                    this.image_count = 5;
                } else if (this.image_count === 5) {
                    document.getElementById("img6").hidden = true;
                    document.getElementById("img7").hidden = false;
                    this.image_count = 6;
                } else if (this.image_count === 6) {
                    document.getElementById("img7").hidden = true;
                    document.getElementById("img8").hidden = false;
                    this.image_count = 7;
                } else if (this.image_count === 7) {
                    document.getElementById("img8").hidden = true;
                    document.getElementById("img9").hidden = false;
                    this.image_count = 8;
                } else if (this.image_count === 8) {
                    document.getElementById("img9").hidden = true;
                    document.getElementById("img10").hidden = false;
                    this.image_count = 9;
                } else if (this.image_count === 9) {
                    document.getElementById("img10").hidden = true;
                    document.getElementById("img11").hidden = false;
                    this.image_count = 10;
                } else if (this.image_count === 10) {
                    document.getElementById("img11").hidden = true;
                    document.getElementById("img12").hidden = false;
                    this.image_count = 11;
                } else if (this.image_count === 11) {
                    document.getElementById("img12").hidden = true;
                    document.getElementById("img13").hidden = false;
                    this.image_count = 12;
                } else if (this.image_count === 12) {
                    document.getElementById("img13").hidden = true;
                    document.getElementById("img14").hidden = false;
                    this.image_count = 13;
                } else if (this.image_count === 13) {
                    document.getElementById("img14").hidden = true;
                    document.getElementById("img15").hidden = false;
                    this.image_count = 14;
                } else if (this.image_count === 14) {
                    document.getElementById("img15").hidden = true;
                    document.getElementById("img16").hidden = false;
                    this.image_count = 15;
                }

            }


        },
        back_img() {
            if (this.image_count === 1) {
                document.getElementById("img2").hidden = true;
                document.getElementById("img1").hidden = false;
                this.image_count = 0;
            } else if (this.image_count === 2) {
                document.getElementById("img3").hidden = true;
                document.getElementById("img2").hidden = false;
                this.image_count = 1;
            } else if (this.image_count === 3) {
                document.getElementById("img4").hidden = true;
                document.getElementById("img3").hidden = false;
                this.image_count = 2;
            } else if (this.image_count === 4) {
                document.getElementById("img5").hidden = true;
                document.getElementById("img4").hidden = false;
                this.image_count = 3;
            } else if (this.image_count === 5) {
                document.getElementById("img6").hidden = true;
                document.getElementById("img5").hidden = false;
                this.image_count = 4;
            } else if (this.image_count === 6) {
                document.getElementById("img7").hidden = true;
                document.getElementById("img6").hidden = false;
                this.image_count = 5;
            } else if (this.image_count === 7) {
                document.getElementById("img8").hidden = true;
                document.getElementById("img7").hidden = false;
                this.image_count = 6;
            } else if (this.image_count === 8) {
                document.getElementById("img9").hidden = true;
                document.getElementById("img8").hidden = false;
                this.image_count = 7;
            } else if (this.image_count === 9) {
                document.getElementById("img10").hidden = true;
                document.getElementById("img9").hidden = false;
                this.image_count = 8;
            } else if (this.image_count === 10) {
                document.getElementById("img11").hidden = true;
                document.getElementById("img10").hidden = false;
                this.image_count = 9;
            } else if (this.image_count === 11) {
                document.getElementById("img12").hidden = true;
                document.getElementById("img11").hidden = false;
                this.image_count = 10;
            } else if (this.image_count === 12) {
                document.getElementById("img13").hidden = true;
                document.getElementById("img12").hidden = false;
                this.image_count = 11;
            } else if (this.image_count === 13) {
                document.getElementById("img14").hidden = true;
                document.getElementById("img13").hidden = false;
                this.image_count = 12;
            } else if (this.image_count === 14) {
                document.getElementById("img15").hidden = true;
                document.getElementById("img14").hidden = false;
                this.image_count = 13;
            } else if (this.image_count === 15) {
                document.getElementById("img16").hidden = true;
                document.getElementById("img15").hidden = false;
                this.image_count = 14;
            }
        },
        load_img() {
            let link = document.querySelectorAll("[id='url_image']");

            let objectLenght = Object.keys(link).length;

            for (let i = 0; i < objectLenght; i++) {
                console.log(link[i].value);

                if (i === 0) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor0.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor0.editorInstance) {
                                this.$refs.tuiImageEditor0.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 1) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor0_.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor0_.editorInstance) {
                                this.$refs.tuiImageEditor0_.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 2) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor1.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor1.editorInstance) {
                                this.$refs.tuiImageEditor1.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 3) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor1_.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor1_.editorInstance) {
                                this.$refs.tuiImageEditor1_.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 4) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor2.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor2.editorInstance) {
                                this.$refs.tuiImageEditor2.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 5) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor2_.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor2_.editorInstance) {
                                this.$refs.tuiImageEditor2_.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 6) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor3.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor3.editorInstance) {
                                this.$refs.tuiImageEditor3.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 7) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor3_.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor3_.editorInstance) {
                                this.$refs.tuiImageEditor3_.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 8) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor4.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor4.editorInstance) {
                                this.$refs.tuiImageEditor4.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 9) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor4_.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor4_.editorInstance) {
                                this.$refs.tuiImageEditor4_.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 10) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor5.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor5.editorInstance) {
                                this.$refs.tuiImageEditor5.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 11) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor5_.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor5_.editorInstance) {
                                this.$refs.tuiImageEditor5_.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 12) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor6.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor6.editorInstance) {
                                this.$refs.tuiImageEditor6.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 13) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor6_.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor6_.editorInstance) {
                                this.$refs.tuiImageEditor6_.editorInstance.ui.activeMenuEvent()
                            }
                        });
                } else if (i === 14) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            this.$refs.tuiImageEditor7.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor7.editorInstance) {
                                this.$refs.tuiImageEditor7.editorInstance.ui.activeMenuEvent()
                            }
                        });
                }
            }
        }
    }
};
</script>


<style scoped>
.logo-img {
    width: 200px;
    height: 90px;
}
</style>