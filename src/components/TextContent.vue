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
            <!-- <div class="flex justify-start gap-1 mb-2 pl-60 font-sans text-xxs text-center text-text2">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-2 h-2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" />
                </svg>

                <p>Please provide complete information for all
                </p>
                <p class="underline decoration-1 decoration-zinc-400">3 items,</p>
                <p>following up period, open both eyes image and close both eyes image, in 1 channel for optimal
                    efficiency of use.</p>
            </div> -->
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
                                        <option value="1, 2" selected>Open, Close</option>
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
                                        <option value="1, 3" selected>Open, Open</option>
                                        <option value="1, 4">Open, Close</option>
                                        <option value="2, 4">Close, Close</option>
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
                                        <option value="3, 4" selected>Open, Close</option>
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
                                        <option value="1, 5" selected>Open, Open</option>
                                        <option value="1, 6">Open, Close</option>
                                        <option value="2, 6">Close, Close</option>
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
                                        <option value="3, 5" selected>Open, Open</option>
                                        <option value="3, 6">Open, Close</option>
                                        <option value="4, 6">Close, Close</option>
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
                                        <option value="5, 6" selected>Open, Close</option>
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
                                        <option value="1, 7" selected>Open, Open</option>
                                        <option value="1, 8">Open, Close</option>
                                        <option value="2, 8">Close, Close</option>
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
                                        <option value="3, 7" selected>Open, Open</option>
                                        <option value="3, 8">Open, Close</option>
                                        <option value="4, 8">Close, Close</option>
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
                                        <option value="5, 7" selected>Open, Open</option>
                                        <option value="5, 8">Open, Close</option>
                                        <option value="6, 8">Close, Close</option>
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
                                        <option value="7, 8" selected>Open, Close</option>
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
                                        <option value="1, 9" selected>Open, Open</option>
                                        <option value="1, 10">Open, Close</option>
                                        <option value="2, 10">Close, Close</option>
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
                                        <option value="3, 9" selected>Open, Open</option>
                                        <option value="3, 10">Open, Close</option>
                                        <option value="4, 10">Close, Close</option>
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
                                        <option value="5, 9" selected>Open, Open</option>
                                        <option value="5, 10">Open, Close</option>
                                        <option value="6, 10">Close, Close</option>
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
                                        <option value="7, 9" selected>Open, Open</option>
                                        <option value="7, 10">Open, Close</option>
                                        <option value="8, 10">Close, Close</option>
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
                                        <option value="9, 10" selected>Open, Close</option>
                                        <option value="None">None</option>
                                    </select>
                                </div>
                            </td>
                        </tr>


                    </tbody>
                </table>


            </div>


        </div>


        <div class="pt-10" id="div_img_first" hidden>
            <!-- 1 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img1_first">
                <div class="w-20 ml-auto flex items-center h-full">
                    <div class="ml-auto mr-auto">

                    </div>
                </div>
                <div class="flex flex-col mt-3">

                    <div class="w-8/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent0">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_0"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_0"></h1>
                                    <h1 class="text-xxss" id="status2_0"></h1>
                                </div>
                            </div>

                            <div class="flex h-full mt-0.75 mb-3 p-2">
                                <img src="" alt="" id="img_src_1" class="mr-auto" style="width: 49%;">
                                <img src="" alt="" id="img_src_2" class="ml-2" style="width: 49%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 mr-auto ml-auto font-sans font-light">
                        <a>
                            <button type="button" @click="preview(1)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(1)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>

                            </button>
                        </a>
                        <a>
                            <button @click="printThis(1)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto mr-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-28 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(1)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>


            <!-- 2 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img2_first" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(2)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-7/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent1">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_1"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_1"></h1>
                                    <h1 class="text-xxss" id="status2_1"></h1>
                                </div>
                            </div>
                            <div class="flex flex-col w-full mt-0.55 p-2">
                                <img src="" alt="" id="img_src_3" class="mr-auto ml-auto" style="width: 99%; height: 50%;">
                                <img src="" alt="" id="img_src_4" class="mr-auto ml-auto mb-2.5 mt-2.5"
                                    style="width: 99%; height: 50%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 pl-48 font-sans font-light">
                        <a>
                            <button type="button" @click="preview(2)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(2)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(2)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-20 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(2)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 3 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img3_first" hidden>
                <button type="button"
                    class="w-28 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(3)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-8/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent2">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_2"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_2"></h1>
                                    <h1 class="text-xxss" id="status2_2"></h1>
                                </div>
                            </div>
                            <div class="flex h-full mt-0.75 mb-3 p-2">
                                <img src="" alt="" id="img_src_5" class="mr-auto" style="width: 49%;">
                                <img src="" alt="" id="img_src_6" class="ml-2" style="width: 49%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 mr-auto ml-auto font-sans font-light">
                        <a>
                            <button type="button" @click="preview(3)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(3)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(3)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto mr-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-28 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(3)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 4 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img4_first" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(4)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-7/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent3">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_3"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_3"></h1>
                                    <h1 class="text-xxss" id="status2_3"></h1>
                                </div>
                            </div>
                            <div class="flex flex-col w-full mt-0.55 p-2">
                                <img src="" alt="" id="img_src_7" class="mr-auto ml-auto" style="width: 99%; height: 50%;">
                                <img src="" alt="" id="img_src_8" class="mr-auto ml-auto mb-2.5 mt-2.5"
                                    style="width: 99%; height: 50%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 pl-48 font-sans font-light">
                        <a>
                            <button type="button" @click="preview(4)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(4)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(4)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-20 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(4)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 5 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img5_first" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(5)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-7/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent4">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_4"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_4"></h1>
                                    <h1 class="text-xxss" id="status2_4"></h1>
                                </div>
                            </div>
                            <div class="flex flex-col w-full mt-0.55 p-2">
                                <img src="" alt="" id="img_src_9" class="mr-auto ml-auto" style="width: 99%; height: 50%;">
                                <img src="" alt="" id="img_src_10" class="mr-auto ml-auto mb-2.5 mt-2.5"
                                    style="width: 99%; height: 50%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 pl-48 font-sans font-light">
                        <a>
                            <button type="button" @click="preview(5)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(5)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(5)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-20 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(5)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 6 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img6_first" hidden>
                <button type="button"
                    class="w-28 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(6)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-8/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent5">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_5"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_5"></h1>
                                    <h1 class="text-xxss" id="status2_5"></h1>
                                </div>
                            </div>
                            <div class="flex h-full mt-0.75 mb-3 p-2">
                                <img src="" alt="" id="img_src_11" class="mr-auto" style="width: 49%;">
                                <img src="" alt="" id="img_src_12" class="ml-2" style="width: 49%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 mr-auto ml-auto font-sans font-light">
                        <a>
                            <button type="button" @click="preview(6)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(6)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(6)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto mr-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-28 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(6)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 7 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img7_first" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(7)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-7/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent6">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_6"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_6"></h1>
                                    <h1 class="text-xxss" id="status2_6"></h1>
                                </div>
                            </div>
                            <div class="flex flex-col w-full mt-0.55 p-2">
                                <img src="" alt="" id="img_src_13" class="mr-auto ml-auto" style="width: 99%; height: 50%;">
                                <img src="" alt="" id="img_src_14" class="mr-auto ml-auto mb-2.5 mt-2.5"
                                    style="width: 99%; height: 50%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 pl-48 font-sans font-light">
                        <a>
                            <button type="button" @click="preview(7)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(7)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(7)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-20 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(7)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 8 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img8_first" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(8)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-7/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent7">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_7"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_7"></h1>
                                    <h1 class="text-xxss" id="status2_7"></h1>
                                </div>
                            </div>
                            <div class="flex flex-col w-full mt-0.55 p-2">
                                <img src="" alt="" id="img_src_15" class="mr-auto ml-auto" style="width: 99%; height: 50%;">
                                <img src="" alt="" id="img_src_16" class="mr-auto ml-auto mb-2.5 mt-2.5"
                                    style="width: 99%; height: 50%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 pl-48 font-sans font-light">
                        <a>
                            <button type="button" @click="preview(8)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(8)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(8)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-20 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(8)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 9 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img9_first" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(9)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-7/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent8">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_8"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_8"></h1>
                                    <h1 class="text-xxss" id="status2_8"></h1>
                                </div>
                            </div>
                            <div class="flex flex-col w-full mt-0.55 p-2">
                                <img src="" alt="" id="img_src_17" class="mr-auto ml-auto" style="width: 99%; height: 50%;">
                                <img src="" alt="" id="img_src_18" class="mr-auto ml-auto mb-2.5 mt-2.5"
                                    style="width: 99%; height: 50%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 pl-48 font-sans font-light">
                        <a>
                            <button type="button" @click="preview(9)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(9)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(9)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-20 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(9)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 10 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img10_first" hidden>
                <button type="button"
                    class="w-28 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(10)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-8/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent9">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_9"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_9"></h1>
                                    <h1 class="text-xxss" id="status2_9"></h1>
                                </div>
                            </div>
                            <div class="flex h-full mt-0.75 mb-3 p-2">
                                <img src="" alt="" id="img_src_19" class="mr-auto" style="width: 49%;">
                                <img src="" alt="" id="img_src_20" class="ml-2" style="width: 49%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 mr-auto ml-auto font-sans font-light">
                        <a>
                            <button type="button" @click="preview(10)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(10)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(10)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto mr-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-28 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(10)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 11 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img11_first" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2"
                    @click="back_image_first(11)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-7/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent10">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_10"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_10"></h1>
                                    <h1 class="text-xxss" id="status2_10"></h1>
                                </div>
                            </div>
                            <div class="flex flex-col w-full mt-0.55 p-2">
                                <img src="" alt="" id="img_src_21" class="mr-auto ml-auto" style="width: 99%; height: 50%;">
                                <img src="" alt="" id="img_src_22" class="mr-auto ml-auto mb-2.5 mt-2.5"
                                    style="width: 99%; height: 50%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 pl-48 font-sans font-light">
                        <a>
                            <button type="button" @click="preview(11)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(11)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(11)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-20 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(11)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 12 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img12_first" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]]"
                    @click="back_image_first(12)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-7/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent11">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_11"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_11"></h1>
                                    <h1 class="text-xxss" id="status2_11"></h1>
                                </div>
                            </div>
                            <div class="flex flex-col w-full mt-0.55 p-2">
                                <img src="" alt="" id="img_src_23" class="mr-auto ml-auto" style="width: 99%; height: 50%;">
                                <img src="" alt="" id="img_src_24" class="mr-auto ml-auto mb-2.5 mt-2.5"
                                    style="width: 99%; height: 50%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 pl-48 font-sans font-light">
                        <a>
                            <button type="button" @click="preview(12)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(12)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(12)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-20 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(12)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 13 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img13_first" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(13)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-7/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent12">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_12"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_12"></h1>
                                    <h1 class="text-xxss" id="status2_12"></h1>
                                </div>
                            </div>
                            <div class="flex flex-col w-full mt-0.55 p-2">
                                <img src="" alt="" id="img_src_25" class="mr-auto ml-auto" style="width: 99%; height: 50%;">
                                <img src="" alt="" id="img_src_26" class="mr-auto ml-auto mb-2.5 mt-2.5"
                                    style="width: 99%; height: 50%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 pl-48 font-sans font-light">
                        <a>
                            <button type="button" @click="preview(13)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(13)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(13)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-20 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(13)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 14 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img14_first" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(14)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-7/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent13">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_13"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_13"></h1>
                                    <h1 class="text-xxss" id="status2_13"></h1>
                                </div>
                            </div>
                            <div class="flex flex-col w-full mt-0.55 p-2">
                                <img src="" alt="" id="img_src_27" class="mr-auto ml-auto" style="width: 99%; height: 50%;">
                                <img src="" alt="" id="img_src_28" class="mr-auto ml-auto mb-2.5 mt-2.5"
                                    style="width: 99%; height: 50%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 pl-48 font-sans font-light">
                        <a>
                            <button type="button" @click="preview(14)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(14)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(14)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-20 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(14)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 15 -->
            <div class="mr-20 ml-20 mt-10 mb-3 bg-bginput rounded-2xl flex" id="img15_first" hidden>
                <button type="button"
                    class="w-28 mr-auto flex items-center hover:bg-[#b6abab] rounded-l-2xl active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(15)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="flex flex-col mt-3">
                    <div class="w-8/12 mr-auto ml-auto bg-white rounded-none">
                        <div class="text-left font-sans ml-3 mr-3 mt-2 p-1" ref="printcontent14">
                            <div class="flex w-full p-1">
                                <h1 class="text-sm ml-1" id="name_14"></h1>
                                <div class="ml-auto font-light p-1">
                                    <h1 class="text-xxsss" id="status1_14"></h1>
                                    <h1 class="text-xxss" id="status2_14"></h1>
                                </div>
                            </div>
                            <div class="flex h-full mt-0.75 mb-3 p-2">
                                <img src="" alt="" id="img_src_29" class="mr-auto" style="width: 49%;">
                                <img src="" alt="" id="img_src_30" class="ml-2" style="width: 49%;">
                            </div>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-2 mb-3 mr-auto ml-auto font-sans font-light">
                        <a>
                            <button type="button" @click="preview(15)"
                                class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Preview<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button type="button" @click="adjust(15)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <a>
                            <button @click="printThis(15)" type="button" :class="{ 'animate-none': downloading }"
                                class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                                <span v-if="!downloading">Download</span>
                                <span v-else>Downloading...</span>
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button" class="w-20 ml-auto flex items-center h-full">

                </button>
            </div>

        </div>

        <div class="pt-3.5" id="div_img_first_preview" hidden>
            <div class="mr-20 ml-20 mt-10 mb-10 bg-transparent flex" id="img1_first_preview" hidden>
                <div class="w-20 ml-auto flex items-center h-full">
                    <div class="ml-auto mr-auto">

                    </div>
                </div>
                <div class="flex flex-col mt-2">
                    <div class="flex flex-row">
                        <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-none">
                            <div class="text-left font-sans ml-2 mr-2 mt-2 p-3" ref="printcontent0_preview">
                                <div class="flex w-full mb-3">
                                    <h1 class="text-lg font-normal ml-1" id="name_0_preview"></h1>
                                    <div class="ml-auto">
                                        <h1 class="text-sm" id="status1_0_preview"></h1>
                                        <h1 class="text-sm mr-1" id="status2_0_preview"></h1>
                                    </div>
                                </div>

                                <div class="flex h-full mb-2 p-2">
                                    <img src="" alt="" id="img_src_1_preview" class="mr-auto" style="width: 49%;">
                                    <img src="" alt="" id="img_src_2_preview" class="ml-auto" style="width: 49%;">
                                </div>
                            </div>
                        </div>
                        <div class="flex item-left w-10 h-8">
                            <button type="button" @click="back_from_previwe()">
                                <svg class="h-7 w-7 text-red-700 hover:text-red-900" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <circle cx="12" cy="12" r="10" />
                                    <line x1="15" y1="9" x2="9" y2="15" />
                                    <line x1="9" y1="9" x2="15" y2="15" />
                                </svg>
                            </button>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 text-center mt-1 mb-4 mr-auto ml-auto font-sans font-light">
                        <a>
                            <button type="button" @click="adjust(1)"
                                class="inline-flex items-center text-white bg-text2 border-lg py-2.5 px-14 focus:outline-none hover:bg-text1 rounded-lg text-lg">Adjust<svg
                                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                    stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75" />
                                </svg>
                            </button>
                        </a>
                        <button @click="printThis_preview(1)" type="button"
                            class="inline-flex text-btn1 bg-[#F6F6F6] border-1 border-blue-800 hover:bg-btn33 py-2.5 px-14 rounded-lg text-lg">
                            Download<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                stroke-width="1.5" stroke="currentColor" class="w-6 h-6 ml-2">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M9 8.25H7.5a2.25 2.25 0 00-2.25 2.25v9a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-9a2.25 2.25 0 00-2.25-2.25H15M9 12l3 3m0 0l3-3m-3 3V2.25" />
                            </svg>
                        </button>
                    </div>
                </div>
                <button type="button" class="ml-auto mr-auto flex items-center" @click="next_image_first(1)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600 hover:h-16 w-16 active:h-16 w-16 focus:h-12 w-12"
                            viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 2 -->
            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img2_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(2)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-10 mb-10 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent1_preview" class="p-3">
                        <div class="text-left ml-2 mr-2 mt-2">
                            <div class="flex w-full mb-3">
                                <h1 id="name_1_preview"></h1>
                                <div class="ml-auto_preview">
                                    <h1 id="status1_1_preview"></h1>
                                    <h1 id="status2_1_preview"></h1>
                                </div>
                            </div>
                            <div class="w-full">
                                <img src="" alt="" id="img_src_3_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                        <div class="text-left ml-20 mr-20 mt-5 mb-5">
                            <div class="w-full">
                                <img src="" alt="" id="img_src_4_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                    </div>
                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(2)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(2)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="ml-auto mr-auto flex items-center hover:bg-[#b6abab] rounded-r-2xl w-28 active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(2)">
                    <div class="ml-auto mr-auto">
                        <svg class="h-12 w-12 text-gray-600" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 3 -->
            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img3_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(3)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent2_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_2_preview"></h1>
                                <h1 id="status1_2_preview" class="ml-auto"></h1>
                                <h1 id="status2_2_preview" class="ml-auto"></h1>
                            </div>
                        </div>
                        <div class="flex h-full">
                            <img src="" alt="" id="img_src_5_preview" class="mr-auto" style="width: 49%;">
                            <img src="" alt="" id="img_src_6_preview" class="ml-auto" style="width: 49%;">
                        </div>
                    </div>
                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(3)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(3)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(3)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img4_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(4)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent3_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_3_preview"></h1>
                                <h1 id="status1_3_preview" class="ml-auto"></h1>
                                <h1 id="status2_3_preview" class="ml-auto"></h1>
                            </div>
                            <div class="w-full">
                                <img src="" alt="" id="img_src_7_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                        <div class="text-left ml-20 mr-20 mt-5 mb-5">
                            <div class="w-full">
                                <img src="" alt="" id="img_src_8_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                    </div>
                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(4)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(4)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(4)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img5_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(5)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent4_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_4_preview"></h1>
                                <h1 id="status1_4_preview" class="ml-auto"></h1>
                                <h1 id="status2_4_preview" class="ml-auto"></h1>
                            </div>
                            <div class="w-full">
                                <img src="" alt="" id="img_src_9_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                        <div class="text-left ml-20 mr-20 mt-5 mb-5">
                            <div class="w-full">
                                <img src="" alt="" id="img_src_10_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                    </div>
                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(5)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(5)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(5)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img6_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(6)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent5_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_5_preview"></h1>
                                <h1 id="status1_5_preview" class="ml-auto"></h1>
                                <h1 id="status2_5_preview" class="ml-auto"></h1>
                            </div>
                        </div>
                        <div class="flex h-full">
                            <img src="" alt="" id="img_src_11_preview" class="mr-auto" style="width: 49%;">
                            <img src="" alt="" id="img_src_12_preview" class="ml-auto" style="width: 49%;">
                        </div>
                    </div>
                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(6)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(6)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(6)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img7_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(7)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent6_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_6_preview"></h1>
                                <h1 id="status1_6_preview" class="ml-auto"></h1>
                                <h1 id="status2_6_preview" class="ml-auto"></h1>
                            </div>
                            <div class="w-full">
                                <img src="" alt="" id="img_src_13_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                        <div class="text-left ml-20 mr-20 mt-5 mb-5">
                            <div class="w-full">
                                <img src="" alt="" id="img_src_14_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                    </div>
                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(7)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(7)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(7)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img8_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(8)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent7_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_7_preview"></h1>
                                <h1 id="status1_7_preview" class="ml-auto"></h1>
                                <h1 id="status2_7_preview" class="ml-auto"></h1>
                            </div>
                            <div class="w-full">
                                <img src="" alt="" id="img_src_15_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                        <div class="text-left ml-20 mr-20 mt-5 mb-5">
                            <div class="w-full">
                                <img src="" alt="" id="img_src_16_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                    </div>
                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(8)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(8)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(8)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img9_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(9)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent8_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_8"></h1>
                                <h1 id="status1_8_preview" class="ml-auto"></h1>
                                <h1 id="status2_8_preview" class="ml-auto"></h1>
                            </div>
                            <div class="w-full">
                                <img src="" alt="" id="img_src_17_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                        <div class="text-left ml-20 mr-20 mt-5 mb-5">
                            <div class="w-full">
                                <img src="" alt="" id="img_src_18_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                    </div>
                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(9)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(9)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(9)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img10_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(10)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent9_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_9_preview"></h1>
                                <h1 id="status1_9_preview" class="ml-auto"></h1>
                                <h1 id="status2_9_preview" class="ml-auto"></h1>
                            </div>
                        </div>
                        <div class="flex h-full">
                            <img src="" alt="" id="img_src_19_preview" class="mr-auto" style="width: 49%;">
                            <img src="" alt="" id="img_src_20_preview" class="ml-auto" style="width: 49%;">
                        </div>
                    </div>
                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(10)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(10)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(10)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img11_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(11)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent10_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_10_preview"></h1>
                                <h1 id="status1_10_preview" class="ml-auto"></h1>
                                <h1 id="status2_10_preview" class="ml-auto"></h1>
                            </div>
                            <div class="w-full">
                                <img src="" alt="" id="img_src_21_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                        <div class="text-left ml-20 mr-20 mt-5 mb-5">
                            <div class="w-full">
                                <img src="" alt="" id="img_src_22_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                    </div>

                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(11)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(11)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(11)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img12_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(12)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent11_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_11_preview"></h1>
                                <h1 id="status1_11_preview" class="ml-auto"></h1>
                                <h1 id="status2_11_preview" class="ml-auto"></h1>
                            </div>
                            <div class="w-full">
                                <img src="" alt="" id="img_src_23_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                        <div class="text-left ml-20 mr-20 mt-5 mb-5">
                            <div class="w-full">
                                <img src="" alt="" id="img_src_24_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                    </div>
                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(12)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(12)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(12)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img13_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(13)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent12_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_12_preview"></h1>
                                <h1 id="status1_12_preview" class="ml-auto"></h1>
                                <h1 id="status2_12_preview" class="ml-auto"></h1>
                            </div>
                            <div class="w-full">
                                <img src="" alt="" id="img_src_25_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                        <div class="text-left ml-20 mr-20 mt-5 mb-5">
                            <div class="w-full">
                                <img src="" alt="" id="img_src_26_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                    </div>

                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(13)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(13)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(13)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img14_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(14)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent13_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_13_preview"></h1>
                                <h1 id="status1_13_preview" class="ml-auto"></h1>
                                <h1 id="status2_13_preview" class="ml-auto"></h1>
                            </div>
                            <div class="w-full">
                                <img src="" alt="" id="img_src_27_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                        <div class="text-left ml-20 mr-20 mt-5 mb-5">
                            <div class="w-full">
                                <img src="" alt="" id="img_src_28_preview" class="mr-auto ml-auto">
                            </div>
                        </div>
                    </div>

                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(14)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(14)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="next_image_first(14)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/right-arrow-removebg-preview.png">
                    </div>
                </button>
            </div>

            <div class="mr-20 ml-20 mt-10 mb-10 bg-[#d0c4c4] rounded-lg flex" id="img15_first_preview" hidden>
                <button type="button"
                    class="w-20 mr-auto flex items-center hover:bg-[#b6abab] active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]"
                    @click="back_image_first(15)">
                    <div class="ml-auto mr-auto">
                        <img alt="" width="40px" src="../image/left-arrow-removebg-preview.png">
                    </div>
                </button>
                <div class="w-11/12 mr-auto ml-auto mt-2 mb-2 bg-white rounded-lg shadow-lg">
                    <div ref="printcontent14_preview" class="p-3">
                        <div class="text-left ml-20 mr-20 mt-5">
                            <div class="flex mb-3">
                                <h1 id="name_14_preview"></h1>
                                <h1 id="status1_14_preview" class="ml-auto"></h1>
                                <h1 id="status2_14_preview" class="ml-auto"></h1>
                            </div>
                        </div>
                        <div class="flex h-full">
                            <img src="" alt="" id="img_src_29_preview" class="mr-auto" style="width: 49%;">
                            <img src="" alt="" id="img_src_30_preview" class="ml-auto" style="width: 49%;">
                        </div>
                    </div>

                    <div class="text-center mt-5 mb-2">
                        <button type="button" @click="adjust(15)"
                            class="inline-flex items-center text-white bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Adjust
                        </button>
                        <button @click="printThis_preview(15)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            Download
                        </button>
                    </div>
                </div>
                <button type="button"
                    class="w-20 ml-auto flex items-center active:bg-[#b6abab] focus:outline-none focus:ring focus:bg-[#ded2d2]">

                </button>
            </div>

        </div>


        <div class="pt-3.5" id="div_img" hidden>
            <!-- 1 -->
            <div class="mr-2 ml-5 mt-4 mb-3 bg-transparent flex" id="img1">
                <div class="w-20 ml-auto flex items-center h-full">
                    <div class="ml-auto mr-auto">

                    </div>
                </div>
                <div class="w-9/12">
                    <div class="w-full mr-auto ml-auto mt-10 bg-white rounded-none">
                        <div class="text-left font-sans ml-5 mr-5 mt-3">
                            <div class="flex w-full">
                                <h1 class="text-sm mt-3" id="ad_name_0"></h1>
                                <div class="ml-auto mt-3">
                                    <h1 class="text-xxss font-light" id="ad_status1_0"></h1>
                                    <h1 class="text-xxss font-light" id="ad_status2_0"></h1>
                                </div>
                            </div>

                            <div class="flex gap-2 h-full mt-2">
                                <div class="mr-auto h-full mb-3 z-0" style="width: 50%;">
                                    <tui-image-editor ref="tuiImageEditor0" :options="options2"
                                        class="text-center"></tui-image-editor>
                                </div>
                                <div class="ml-auto h-full mb-3 z-0" style="width: 50%;">
                                    <tui-image-editor ref="tuiImageEditor0_" :options="options2"
                                        class="text-center"></tui-image-editor>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="text-center font-sans font-light">
                        <a>
                            <button @click="finish(1)" type="button"
                                class="inline-flex items-center text-white font-sans font-light bg-btn1 border-lg py-2.5 px-14 mt-3 focus:outline-none hover:bg-btn11 rounded-lg text-lg">
                                Finish<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button" class="ml-auto flex items-center" @click="next_img">
                    <div class="ml-auto mr-10">
                        <svg class="h-12 w-12 text-gray-600 hover:h-16 w-16 active:h-16 w-16 focus:h-12 w-12"
                            viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 2 -->
            <div class="mr-20 ml-20 mt-4 mb-3 bg-transparent flex" id="img2" hidden>
                <button type="button" class="mr-auto flex items-center" @click="back_img">
                    <div class="ml-10 mr-auto">
                        <svg class="h-12 w-12 text-gray-600 hover:h-16 w-16 active:h-16 w-16 focus:h-12 w-12"
                            viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round">
                            <polyline points="15 18 9 12 15 6" />
                        </svg>
                    </div>
                </button>
                <div class="w-7/12">
                    <div class="w-full mr-auto ml-auto mt-10 bg-white rounded-none">
                        <div class="text-left font-sans ml-5 mr-5 mt-3">
                            <div class="flex w-full">
                                <h1 class="text-sm mt-3" id="ad_name_1"></h1>
                                <div class="ml-auto mt-3">
                                    <h1 id="ad_status1_1" class="ml-auto text-xxss font-light"></h1>
                                    <h1 id="ad_status2_1" class="ml-auto text-xxss font-light"></h1>
                                </div>
                            </div>
                        </div>
                        <div class="text-left ml-5 mr-5 mt-2">
                            <div class="flex h-full">
                                <tui-image-editor ref="tuiImageEditor1" :options="options"></tui-image-editor>
                            </div>
                            <div class="flex h-full mt-2 pb-3">
                                <tui-image-editor ref="tuiImageEditor1_" :options="options"></tui-image-editor>
                            </div>
                        </div>
                    </div>
                    <div class="text-center font-sans font-light">
                        <a>
                            <button @click="finish(2)" type="button"
                                class="inline-flex items-center text-white font-sans font-light bg-btn1 border-lg py-2.5 px-14 mt-3 focus:outline-none hover:bg-btn11 rounded-lg text-lg">
                                finish<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-6 h-6 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                            </button>
                        </a>
                    </div>
                </div>
                <button type="button" class="ml-auto flex items-center" @click="next_img">
                    <div class="ml-auto mr-10">
                        <svg class="h-12 w-12 text-gray-600 hover:h-16 w-16 active:h-16 w-16 focus:h-12 w-12"
                            viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                            stroke-linejoin="round">
                            <polyline points="9 18 15 12 9 6" />
                        </svg>
                    </div>
                </button>
            </div>

            <!-- 3 -->
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
                            <h1 id="ad_name_2"></h1>
                            <h1 id="ad_status1_2" class="ml-auto"></h1>
                            <h1 id="ad_status2_2" class="ml-auto"></h1>
                        </div>
                    </div>

                    <div class="flex h-full">
                        <div class="mr-auto h-full" style="width: 50%;">
                            <tui-image-editor ref="tuiImageEditor2" :options="options2"
                                class="text-center"></tui-image-editor>
                        </div>
                        <div class="ml-auto h-full " style="width: 50%;">
                            <tui-image-editor ref="tuiImageEditor2_" :options="options2"
                                class="text-center"></tui-image-editor>
                        </div>
                    </div>

                    <div class="text-center">
                        <button @click="finish(3)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 4 -->
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
                            <h1 id="ad_name_3"></h1>
                            <h1 id="ad_status1_3" class="ml-auto"></h1>
                            <h1 id="ad_status2_3" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor3" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor3_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(4)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 5 -->
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
                            <h1 id="ad_name_4"></h1>
                            <h1 id="ad_status1_4" class="ml-auto"></h1>
                            <h1 id="ad_status2_4" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor4" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor4_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(5)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 6 -->
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
                            <h1 id="ad_name_5"></h1>
                            <h1 id="ad_status1_5" class="ml-auto"></h1>
                            <h1 id="ad_status2_5" class="ml-auto"></h1>
                        </div>
                    </div>
                    <div class="flex h-full">
                        <div class="mr-auto h-full" style="width: 50%;">
                            <tui-image-editor ref="tuiImageEditor5" :options="options2"
                                class="text-center"></tui-image-editor>
                        </div>
                        <div class="ml-auto h-full " style="width: 50%;">
                            <tui-image-editor ref="tuiImageEditor5_" :options="options2"
                                class="text-center"></tui-image-editor>
                        </div>
                    </div>

                    <div class="text-center">
                        <button @click="finish(6)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 7 -->
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
                            <h1 id="ad_name_6"></h1>
                            <h1 id="ad_status1_6" class="ml-auto"></h1>
                            <h1 id="ad_status2_6" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor6" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor6_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(7)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 8 -->
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
                            <h1 id="ad_name_7"></h1>
                            <h1 id="ad_status1_7" class="ml-auto"></h1>
                            <h1 id="ad_status2_7" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor7" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor7_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(8)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 9 -->
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
                            <h1 id="ad_name_8"></h1>
                            <h1 id="ad_status1_8" class="ml-auto"></h1>
                            <h1 id="ad_status2_8" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor8" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor8_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(9)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 10 -->
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
                            <h1 id="ad_name_9"></h1>
                            <h1 id="ad_status1_9" class="ml-auto"></h1>
                            <h1 id="ad_status2_9" class="ml-auto"></h1>
                        </div>
                    </div>
                    <div class="flex h-full">
                        <div class="mr-auto h-full" style="width: 50%;">
                            <tui-image-editor ref="tuiImageEditor9" :options="options2"
                                class="text-center"></tui-image-editor>
                        </div>
                        <div class="ml-auto h-full " style="width: 50%;">
                            <tui-image-editor ref="tuiImageEditor9_" :options="options2"
                                class="text-center"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(10)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 11 -->
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
                            <h1 id="ad_name_10"></h1>
                            <h1 id="ad_status1_10" class="ml-auto"></h1>
                            <h1 id="ad_status2_10" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor10" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor10_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(11)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 12 -->
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
                            <h1 id="ad_name_11"></h1>
                            <h1 id="ad_status1_11" class="ml-auto"></h1>
                            <h1 id="ad_status2_11" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor11" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor11_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(12)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 13 -->
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
                            <h1 id="ad_name_12"></h1>
                            <h1 id="ad_status1_12" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor12" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex">
                            <h1 id="ad_status2_12" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor12_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(13)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 14 -->
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
                            <h1 id="ad_name_13"></h1>
                            <h1 id="ad_status1_13" class="ml-auto"></h1>
                            <h1 id="ad_status2_13" class="ml-auto"></h1>
                        </div>
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor13" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-left ml-20 mr-20 mt-5 mb-5">
                        <div class="flex h-full">
                            <tui-image-editor ref="tuiImageEditor13_" :options="options"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(14)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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

            <!-- 15 -->
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
                            <h1 id="ad_name_14"></h1>
                            <h1 id="ad_status1_14" class="ml-auto"></h1>
                            <h1 id="ad_status2_14" class="ml-auto"></h1>
                        </div>
                    </div>
                    <div class="flex h-full">
                        <div class="mr-auto h-full" style="width: 50%;">
                            <tui-image-editor ref="tuiImageEditor14" :options="options2"
                                class="text-center"></tui-image-editor>
                        </div>
                        <div class="ml-auto h-full " style="width: 50%;">
                            <tui-image-editor ref="tuiImageEditor14_" :options="options2"
                                class="text-center"></tui-image-editor>
                        </div>
                    </div>
                    <div class="text-center">
                        <button @click="finish(15)" type="button"
                            class="inline-flex  text-white bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14 mt-5 mb-2 rounded-lg text-lg">
                            finish
                        </button>
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
                class="inline-flex items-center text-white font-sans font-light bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg">Next
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 ml-2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M12.75 15l3-3m0 0l-3-3m3 3h-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>

            </button>

            <button id="btn_des_next1" type="button" @click="back_to_main"
                class="me-2 inline-flex items-center bg-bg font-sans font-light hover:bg-btn33 text-btn1 border-1 border-btn1 py-2.2 px-14 focus:outline-none rounded-lg text-lg"
                hidden>Back<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 ml-2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M11.25 9l-3 3m0 0l3 3m-3-3h7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
            </button>

            <button id="btn_des_next2" type="button" @click="submit"
                class="inline-flex items-center text-white bg-btn1 font-sans font-light border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg"
                hidden>Submit
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 ml-2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M12.75 15l3-3m0 0l-3-3m3 3h-7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>

            </button>


            <button id="btn_img_back" type="button" @click="back_to_img_first"
                class="me-2 inline-flex items-center text-white font-sans font-light bg-cyan-500 hover:bg-cyan-600 py-2.5 px-14  rounded-lg text-lg"
                hidden>Back

            </button>

            <button id="btn_img_first_back" type="button" @click="back_to_des"
                class="me-2 inline-flex items-center bg-bg font-sans font-light hover:bg-btn33 text-btn1 border-1 border-btn1 py-2.2 px-14 focus:outline-none rounded-lg text-lg"
                hidden>Back<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 ml-2">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M11.25 9l-3 3m0 0l3 3m-3-3h7.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
            </button>

            <button id="btn_download_all" type="button" @click="downloadAll"
                class="me-2 inline-flex items-center text-white font-sans font-light bg-btn1 border-lg py-2.5 px-14 focus:outline-none hover:bg-btn11 rounded-lg text-lg"
                hidden>
                Download All<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6 ml-1">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M7.5 7.5h-.75A2.25 2.25 0 004.5 9.75v7.5a2.25 2.25 0 002.25 2.25h7.5a2.25 2.25 0 002.25-2.25v-7.5a2.25 2.25 0 00-2.25-2.25h-.75m-6 3.75l3 3m0 0l3-3m-3 3V1.5m6 9h.75a2.25 2.25 0 012.25 2.25v7.5a2.25 2.25 0 01-2.25 2.25h-7.5a2.25 2.25 0 01-2.25-2.25v-.75" />
                </svg>

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
import html2canvas from 'html2canvas';


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

            image_get_1: null,
            image_get_2: null,
            image_get_3: null,
            image_get_4: null,
            image_get_5: null,
            image_get_6: null,
            image_get_7: null,
            image_get_8: null,
            image_get_9: null,
            image_get_10: null,
            image_get_11: null,
            image_get_12: null,
            image_get_13: null,
            image_get_14: null,
            image_get_15: null,

            text_follow_1: "",
            text_follow_2: "",
            text_follow_3: "",
            text_follow_4: "",
            text_follow_5: "",

            downloading: false,
            showTooltip: false,
            page_image_adjust: 0,
            image_count: 0,
            image_end: 0,
            filelist: [], // Store our uploaded files,
            useDefaultUI: true,
            options: {
                includeUI: {
                    menu: [
                        "resize",
                        "crop",
                        "flip",
                        "rotate",
                        "text",
                    ],
                    menuBarPosition: 'top',
                    uiSize: {
                        width: '800px',
                        height: '450px'
                    },

                },
                cssMaxWidth: 370,
                cssMaxHeight: 800,
            },
            options2: {
                includeUI: {
                    menu: [
                        "resize",
                        "crop",
                        "flip",
                        "rotate",
                        "text",
                    ],
                    menuBarPosition: 'top',
                    uiSize: {
                        width: '508px',
                        height: '700px',
                    },
                },
                cssMaxWidth: 360,
                cssMaxHeight: 800,
            },
        }
    },
    methods: {
        showInfo() {
            this.showTooltip = true;
        },
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
            } else if (item === 'f3_2') {
                document.getElementById("label_f3_2").hidden = false;
                document.getElementById("img_f3_2").hidden = true;
                document.getElementById("btn_f3_2").hidden = true;
                this.image_f3_2 = null;
                this.files_f3_2 = null;
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
            } else if (this.current == 2) {
                if (this.text_follow_2 == '' || this.image_f1_1 == null || this.image_f1_2 == null) {
                    alert('Please enter the information before clicking the next button');
                    return;
                }
            } else if (this.current == 3) {
                if (this.text_follow_3 == '' || this.image_f2_1 == null || this.image_f2_2 == null) {
                    alert('Please enter the information before clicking the next button');
                    return;
                }
            } else if (this.current == 4) {
                if (this.text_follow_4 == '' || this.image_f3_1 == null || this.image_f3_2 == null) {
                    alert('Please enter the information before clicking the next button');
                    return;
                }
            } else if (this.current == 5) {
                if (this.text_follow_5 == '' || this.image_f4_1 == null || this.image_f4_2 == null) {
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
            document.getElementById("div_img_first").hidden = true;
            document.getElementById("btn_img_first_back").hidden = true;
            document.getElementById("btn_download_all").hidden = true;


            this.image_count = 0;
            document.getElementById("btn_img_back").hidden = true;
            document.getElementById("div_img_first").hidden = true;
        },
        back_to_img_first() {
            document.getElementById("div_img").hidden = true;
            document.getElementById("btn_img_back").hidden = false;
            document.getElementById("div_img_first").hidden = false;
            document.getElementById("btn_download_all").hidden = false;
            document.getElementById("img1").hidden = true;
            document.getElementById("img2").hidden = true;
            document.getElementById("img3").hidden = true;
            document.getElementById("img4").hidden = true;
            document.getElementById("img5").hidden = true;
            document.getElementById("img6").hidden = true;
            document.getElementById("img7").hidden = true;
            document.getElementById("img8").hidden = true;
            document.getElementById("img9").hidden = true;
            document.getElementById("img10").hidden = true;
            document.getElementById("img11").hidden = true;
            document.getElementById("img12").hidden = true;
            document.getElementById("img13").hidden = true;
            document.getElementById("img14").hidden = true;
            document.getElementById("img15").hidden = true;


            this.image_count = 0;
        },
        submit() {
            let formData = new FormData();

            let files_1 = document.getElementById("select_1").value;
            let files_2 = document.getElementById("select_2").value;
            let files_3 = document.getElementById("select_3").value;
            let files_4 = document.getElementById("select_4").value;
            let files_5 = document.getElementById("select_5").value;
            let files_6 = document.getElementById("select_6").value;
            let files_7 = document.getElementById("select_7").value;
            let files_8 = document.getElementById("select_8").value;
            let files_9 = document.getElementById("select_9").value;
            let files_10 = document.getElementById("select_10").value;
            let files_11 = document.getElementById("select_11").value;
            let files_12 = document.getElementById("select_12").value;
            let files_13 = document.getElementById("select_13").value;
            let files_14 = document.getElementById("select_14").value;
            let files_15 = document.getElementById("select_15").value;

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


            formData.append("files 1", files_1);
            formData.append("files 2", files_2);
            formData.append("files 3", files_3);
            formData.append("files 4", files_4);
            formData.append("files 5", files_5);
            formData.append("files 6", files_6);
            formData.append("files 7", files_7);
            formData.append("files 8", files_8);
            formData.append("files 9", files_9);
            formData.append("files 10", files_10);
            formData.append("files 11", files_11);
            formData.append("files 12", files_12);
            formData.append("files 13", files_13);
            formData.append("files 14", files_14);
            formData.append("files 15", files_15);


            formData.append("type 1", `${this.text_follow_1}`);
            formData.append("type 2", `${this.text_follow_1} and ${this.text_follow_2}`);
            formData.append("type 3", `${this.text_follow_2}`);
            formData.append("type 4", `${this.text_follow_1} and ${this.text_follow_3}`);
            formData.append("type 5", `${this.text_follow_2} and ${this.text_follow_3}`);
            formData.append("type 6", `${this.text_follow_3}`);
            formData.append("type 7", `${this.text_follow_1} and ${this.text_follow_4}`);
            formData.append("type 8", `${this.text_follow_2} and ${this.text_follow_4}`);
            formData.append("type 9", `${this.text_follow_3} and ${this.text_follow_4}`);
            formData.append("type 10", `${this.text_follow_4}`);
            formData.append("type 11", `${this.text_follow_1} and ${this.text_follow_5}`);
            formData.append("type 12", `${this.text_follow_2} and ${this.text_follow_5}`);
            formData.append("type 13", `${this.text_follow_3} and ${this.text_follow_5}`);
            formData.append("type 14", `${this.text_follow_4} and ${this.text_follow_5}`);
            formData.append("type 15", `${this.text_follow_5}`);


            // var html = "";
            axios.post('http://127.0.0.1:5000/upload_files',
                // axios.post('http://localhost:3000/upload_files',
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }
            ).then(function (response) {
                let data = response.data;
                let objectLenght = Object.keys(data).length;
                let html = "";
                for (let i = 0; i < objectLenght; i++) {
                    html = `${data[i].name}`;
                    document.getElementById(`name_${i}`).innerText = html;
                    document.getElementById(`ad_name_${i}`).innerText = html;
                    document.getElementById(`name_${i}_preview`).innerText = html;

                    html = `(R1) EBH: ${data[i][0][0]} px OSA: ${data[i][0][1]} px  (L1) EBH: ${data[i][0][2]} px  OSA: ${data[i][0][3]} px`;
                    document.getElementById(`status1_${i}`).innerText = html;
                    document.getElementById(`ad_status1_${i}`).innerText = html;
                    document.getElementById(`status1_${i}_preview`).innerText = html;
                    html = `(R2) EBH: ${data[i][1][0]} px OSA: ${data[i][1][1]} px  (L2) EBH: ${data[i][1][2]} px  OSA: ${data[i][1][3]} px`;
                    document.getElementById(`status2_${i}`).innerText = html;
                    document.getElementById(`ad_status2_${i}`).innerText = html;
                    document.getElementById(`status2_${i}_preview`).innerText = html;

                    document.getElementById('link').innerHTML += `<input type='text' id='url_image' value='${data[i].url1}'>`;
                    document.getElementById('link').innerHTML += `<input type='text' id='url_image' value='${data[i].url2}'>`;

                }
                document.getElementById("div_des").hidden = true;
                document.getElementById("des").hidden = true;
                document.getElementById("btn_des_next1").hidden = true;
                document.getElementById("btn_des_next2").hidden = true;
                document.getElementById("div_img").hidden = true;
                document.getElementById("div_img_first").hidden = false;
                document.getElementById("btn_img_first_back").hidden = false;
                document.getElementById("btn_img_back").hidden = true;
                document.getElementById("btn_download_all").hidden = false;

            }).then(() => {
                let link = document.querySelectorAll("[id='url_image']");

                let objectLenght = Object.keys(link).length;

                for (let i = 0; i < objectLenght; i++) {
                    console.log(link[i].value);

                    if (i === 0) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_1").src = objectURL;
                                document.getElementById("img_src_1_preview").src = objectURL;
                            });
                    } else if (i === 1) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_2").src = objectURL;
                                document.getElementById("img_src_2_preview").src = objectURL;
                            });
                    } else if (i === 2) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_3").src = objectURL;
                                document.getElementById("img_src_3_preview").src = objectURL;
                            });
                    } else if (i === 3) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_4").src = objectURL;
                                document.getElementById("img_src_4_preview").src = objectURL;
                            });
                    } else if (i === 4) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_5").src = objectURL;
                                document.getElementById("img_src_5_preview").src = objectURL;
                            });
                    } else if (i === 5) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_6").src = objectURL;
                                document.getElementById("img_src_6_preview").src = objectURL;
                            });
                    } else if (i === 6) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_7").src = objectURL;
                                document.getElementById("img_src_7_preview").src = objectURL;
                            });
                    } else if (i === 7) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_8").src = objectURL;
                                document.getElementById("img_src_8_preview").src = objectURL;
                            });
                    } else if (i === 8) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_9").src = objectURL;
                                document.getElementById("img_src_9_preview").src = objectURL;
                            });
                    } else if (i === 9) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_10").src = objectURL;
                                document.getElementById("img_src_10_preview").src = objectURL;
                            });
                    } else if (i === 10) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_11").src = objectURL;
                                document.getElementById("img_src_11_preview").src = objectURL;
                            });
                    } else if (i === 11) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_12").src = objectURL;
                                document.getElementById("img_src_12_preview").src = objectURL;
                            });
                    } else if (i === 12) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_13").src = objectURL;
                                document.getElementById("img_src_13_preview").src = objectURL;
                            });
                    } else if (i === 13) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_14").src = objectURL;
                                document.getElementById("img_src_14_preview").src = objectURL;
                            });
                    } else if (i === 14) {
                        fetch(link[i].value)
                            .then(res => res.blob())
                            .then(blob => {
                                var objectURL = URL.createObjectURL(blob);
                                document.getElementById("img_src_15").src = objectURL;
                                document.getElementById("img_src_15_preview").src = objectURL;
                            });
                    }
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
        next_image_first(page) {
            let link1 = document.querySelectorAll("[id='url_image']");

            let objectLenght1 = Object.keys(link1).length;

            if (page === 1 && page < objectLenght1 / 2) {
                document.getElementById("img1_first").hidden = true;
                document.getElementById("img2_first").hidden = false;
                this.image_count = 1;
            } else if (page === 2 && page < objectLenght1 / 2) {
                document.getElementById("img2_first").hidden = true;
                document.getElementById("img3_first").hidden = false;
                this.image_count = 2;
            } else if (page === 3 && page < objectLenght1 / 2) {
                document.getElementById("img3_first").hidden = true;
                document.getElementById("img4_first").hidden = false;
                this.image_count = 3;
            } else if (page === 4 && page < objectLenght1 / 2) {
                document.getElementById("img4_first").hidden = true;
                document.getElementById("img5_first").hidden = false;
                this.image_count = 4;
            } else if (page === 5 && page < objectLenght1 / 2) {
                document.getElementById("img5_first").hidden = true;
                document.getElementById("img6_first").hidden = false;
                this.image_count = 5;
            } else if (page === 6 && page < objectLenght1 / 2) {
                document.getElementById("img6_first").hidden = true;
                document.getElementById("img7_first").hidden = false;
                this.image_count = 6;
            } else if (page === 7 && page < objectLenght1 / 2) {
                document.getElementById("img7_first").hidden = true;
                document.getElementById("img8_first").hidden = false;
                this.image_count = 7;
            } else if (page === 8 && page < objectLenght1 / 2) {
                document.getElementById("img8_first").hidden = true;
                document.getElementById("img9_first").hidden = false;
                this.image_count = 8;
            } else if (page === 9 && page < objectLenght1 / 2) {
                document.getElementById("img9_first").hidden = true;
                document.getElementById("img10_first").hidden = false;
                this.image_count = 9;
            } else if (page === 10 && page < objectLenght1 / 2) {
                document.getElementById("img10_first").hidden = true;
                document.getElementById("img11_first").hidden = false;
                this.image_count = 10;
            } else if (page === 11 && page < objectLenght1 / 2) {
                document.getElementById("img11_first").hidden = true;
                document.getElementById("img12_first").hidden = false;
                this.image_count = 11;
            } else if (page === 12 && page < objectLenght1 / 2) {
                document.getElementById("img12_first").hidden = true;
                document.getElementById("img13_first").hidden = false;
                this.image_count = 12;
            } else if (page === 13 && page < objectLenght1 / 2) {
                document.getElementById("img13_first").hidden = true;
                document.getElementById("img14_first").hidden = false;
            } else if (page === 14 && page < objectLenght1 / 2) {
                document.getElementById("img14_first").hidden = true;
                document.getElementById("img15_first").hidden = false;
            }
        },
        back_image_first(page) {
            if (page === 2) {
                document.getElementById("img2_first").hidden = true;
                document.getElementById("img1_first").hidden = false;
            } else if (page === 3) {
                document.getElementById("img3_first").hidden = true;
                document.getElementById("img2_first").hidden = false;
            } else if (page === 4) {
                document.getElementById("img4_first").hidden = true;
                document.getElementById("img3_first").hidden = false;
            } else if (page === 5) {
                document.getElementById("img5_first").hidden = true;
                document.getElementById("img4_first").hidden = false;
            } else if (page === 6) {
                document.getElementById("img6_first").hidden = true;
                document.getElementById("img5_first").hidden = false;
            } else if (page === 7) {
                document.getElementById("img7_first").hidden = true;
                document.getElementById("img6_first").hidden = false;
            } else if (page === 8) {
                document.getElementById("img8_first").hidden = true;
                document.getElementById("img7_first").hidden = false;
            } else if (page === 9) {
                document.getElementById("img9_first").hidden = true;
                document.getElementById("img8_first").hidden = false;
            } else if (page === 10) {
                document.getElementById("img10_first").hidden = true;
                document.getElementById("img9_first").hidden = false;
            } else if (page === 11) {
                document.getElementById("img11_first").hidden = true;
                document.getElementById("img10_first").hidden = false;
            } else if (page === 12) {
                document.getElementById("img12_first").hidden = true;
                document.getElementById("img11_first").hidden = false;
            } else if (page === 13) {
                document.getElementById("img13_first").hidden = true;
                document.getElementById("img12_first").hidden = false;
            } else if (page === 14) {
                document.getElementById("img14_first").hidden = true;
                document.getElementById("img13_first").hidden = false;
            } else if (page === 15) {
                document.getElementById("img15_first").hidden = true;
                document.getElementById("img14_first").hidden = false;
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
        }, adjust(page) {
            document.getElementById("div_img").hidden = false;
            document.getElementById("btn_img_back").hidden = false;
            document.getElementById("btn_img_first_back").hidden = true;
            document.getElementById("div_img_first_preview").hidden = true;
            if (page === 1) {
                this.image_count = 0;
                document.getElementById("img1").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img1_first_preview").hidden = true;
            } else if (page === 2) {
                this.image_count = 1;
                document.getElementById("img2").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img2_first_preview").hidden = true;
            } else if (page === 3) {
                this.image_count = 2;
                document.getElementById("img3").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img3_first_preview").hidden = true;
            } else if (page === 4) {
                this.image_count = 3;
                document.getElementById("img4").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img4_first_preview").hidden = true;
            } else if (page === 5) {
                this.image_count = 4;
                document.getElementById("img5").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img5_first_preview").hidden = true;
            } else if (page === 6) {
                this.image_count = 5;
                document.getElementById("img6").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img6_first_preview").hidden = true;
            } else if (page === 7) {
                this.image_count = 6;
                document.getElementById("img7").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img7_first_preview").hidden = true;
            } else if (page === 8) {
                this.image_count = 7;
                document.getElementById("img8").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img8_first_preview").hidden = true;
            } else if (page === 9) {
                this.image_count = 8;
                document.getElementById("img9").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img9_first_preview").hidden = true;
            } else if (page === 10) {
                this.image_count = 9;
                document.getElementById("img10").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img10_first_preview").hidden = true;
            } else if (page === 11) {
                this.image_count = 10;
                document.getElementById("img11").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img11_first_preview").hidden = true;
            } else if (page === 12) {
                this.image_count = 11;
                document.getElementById("img12").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img12_first_preview").hidden = true;
            } else if (page === 13) {
                this.image_count = 12;
                document.getElementById("img13").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img13_first_preview").hidden = true;
            } else if (page === 14) {
                this.image_count = 13;
                document.getElementById("img14").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img14_first_preview").hidden = true;
            } else if (page === 15) {
                this.image_count = 14;
                document.getElementById("img15").hidden = false;
                document.getElementById("div_img_first").hidden = true;
                document.getElementById("img15_first_preview").hidden = true;
            }


            let link = document.querySelectorAll("[id='url_image']");

            let objectLenght = Object.keys(link).length;

            for (let i = 0; i < objectLenght; i++) {
                console.log(link[i].value);

                if (i === 0) {
                    fetch(link[i].value)
                        .then(res => res.blob())
                        .then(blob => {
                            var objectURL = URL.createObjectURL(blob);
                            document.getElementById("img_src_1").src = objectURL;
                            document.getElementById("img_src_1_preview").src = objectURL;
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
                            document.getElementById("img_src_2").src = objectURL;
                            document.getElementById("img_src_2_preview").src = objectURL;
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
                            document.getElementById("img_src_3").src = objectURL;
                            document.getElementById("img_src_3_preview").src = objectURL;
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
                            document.getElementById("img_src_4").src = objectURL;
                            document.getElementById("img_src_4_preview").src = objectURL;
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
                            document.getElementById("img_src_5").src = objectURL;
                            document.getElementById("img_src_5_preview").src = objectURL;
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
                            document.getElementById("img_src_6").src = objectURL;
                            document.getElementById("img_src_6_preview").src = objectURL;
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
                            document.getElementById("img_src_7").src = objectURL;
                            document.getElementById("img_src_7_preview").src = objectURL;
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
                            document.getElementById("img_src_8").src = objectURL;
                            document.getElementById("img_src_8_preview").src = objectURL;
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
                            document.getElementById("img_src_9").src = objectURL;
                            document.getElementById("img_src_9_preview").src = objectURL;
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
                            document.getElementById("img_src_10").src = objectURL;
                            document.getElementById("img_src_10_preview").src = objectURL;
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
                            document.getElementById("img_src_11").src = objectURL;
                            document.getElementById("img_src_11_preview").src = objectURL;
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
                            document.getElementById("img_src_12").src = objectURL;
                            document.getElementById("img_src_12_preview").src = objectURL;
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
                            document.getElementById("img_src_13").src = objectURL;
                            document.getElementById("img_src_13_preview").src = objectURL;
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
                            document.getElementById("img_src_14").src = objectURL;
                            document.getElementById("img_src_14_preview").src = objectURL;
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
                            document.getElementById("img_src_15").src = objectURL;
                            document.getElementById("img_src_15_preview").src = objectURL;
                            this.$refs.tuiImageEditor7.invoke('loadImageFromURL', objectURL, '222');
                            if (this.$refs.tuiImageEditor7.editorInstance) {
                                this.$refs.tuiImageEditor7.editorInstance.ui.activeMenuEvent()
                            }
                        });
                }
            }
        },
        finish(num) {
            if (num === 1) {
                let canvasSize1 = this.$refs.tuiImageEditor0.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor0.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor0_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor0_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_1").src = url1;
                document.getElementById("img_src_2").src = url2;

                document.getElementById("img_src_1_preview").src = url1;
                document.getElementById("img_src_2_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img1").hidden = true;
                document.getElementById("img1_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 2) {
                let canvasSize1 = this.$refs.tuiImageEditor1.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor1.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor1_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor1_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_3").src = url1;
                document.getElementById("img_src_4").src = url2;

                document.getElementById("img_src_3_preview").src = url1;
                document.getElementById("img_src_4_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img2").hidden = true;
                document.getElementById("img2_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 3) {
                let canvasSize1 = this.$refs.tuiImageEditor2.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor2.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor2_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor2_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_5").src = url1;
                document.getElementById("img_src_6").src = url2;

                document.getElementById("img_src_5_preview").src = url1;
                document.getElementById("img_src_6_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img3").hidden = true;
                document.getElementById("img3_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 4) {
                let canvasSize1 = this.$refs.tuiImageEditor3.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor3.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor3_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor3_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_7").src = url1;
                document.getElementById("img_src_8").src = url2;

                document.getElementById("img_src_7_preview").src = url1;
                document.getElementById("img_src_8_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img4").hidden = true;
                document.getElementById("img4_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 5) {
                let canvasSize1 = this.$refs.tuiImageEditor4.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor4.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor4_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor4_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_9").src = url1;
                document.getElementById("img_src_10").src = url2;

                document.getElementById("img_src_9_preview").src = url1;
                document.getElementById("img_src_10_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img5").hidden = true;
                document.getElementById("img5_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 6) {
                let canvasSize1 = this.$refs.tuiImageEditor5.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor5.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor5_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor5_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_11").src = url1;
                document.getElementById("img_src_12").src = url2;

                document.getElementById("img_src_11_preview").src = url1;
                document.getElementById("img_src_12_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img6").hidden = true;
                document.getElementById("img6_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 7) {
                let canvasSize1 = this.$refs.tuiImageEditor6.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor6.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor6_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor6_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_13").src = url1;
                document.getElementById("img_src_14").src = url2;

                document.getElementById("img_src_13_preview").src = url1;
                document.getElementById("img_src_14_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img7").hidden = true;
                document.getElementById("img7_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 8) {
                let canvasSize1 = this.$refs.tuiImageEditor7.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor7.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor7_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor7_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_15").src = url1;
                document.getElementById("img_src_16").src = url2;

                document.getElementById("img_src_15_preview").src = url1;
                document.getElementById("img_src_16_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img8").hidden = true;
                document.getElementById("img8_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 9) {
                let canvasSize1 = this.$refs.tuiImageEditor8.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor8.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor8_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor8_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_17").src = url1;
                document.getElementById("img_src_18").src = url2;

                document.getElementById("img_src_17_preview").src = url1;
                document.getElementById("img_src_18_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img9").hidden = true;
                document.getElementById("img9_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 10) {
                let canvasSize1 = this.$refs.tuiImageEditor9.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor9.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor9_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor9_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_19").src = url1;
                document.getElementById("img_src_20").src = url2;

                document.getElementById("img_src_19_preview").src = url1;
                document.getElementById("img_src_20_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img10").hidden = true;
                document.getElementById("img10_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 11) {
                let canvasSize1 = this.$refs.tuiImageEditor10.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor10.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor10_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor10_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_21").src = url1;
                document.getElementById("img_src_22").src = url2;

                document.getElementById("img_src_21_preview").src = url1;
                document.getElementById("img_src_22_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img11").hidden = true;
                document.getElementById("img11_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 12) {
                let canvasSize1 = this.$refs.tuiImageEditor11.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor11.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor11_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor11_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_23").src = url1;
                document.getElementById("img_src_24").src = url2;

                document.getElementById("img_src_23_preview").src = url1;
                document.getElementById("img_src_24_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img12").hidden = true;
                document.getElementById("img12_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 13) {
                let canvasSize1 = this.$refs.tuiImageEditor12.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor12.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor12_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor12_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_25").src = url1;
                document.getElementById("img_src_26").src = url2;

                document.getElementById("img_src_25_preview").src = url1;
                document.getElementById("img_src_26_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img13").hidden = true;
                document.getElementById("img13_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 14) {
                let canvasSize1 = this.$refs.tuiImageEditor13.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor13.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor13_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor13_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_27").src = url1;
                document.getElementById("img_src_28").src = url2;

                document.getElementById("img_src_27_preview").src = url1;
                document.getElementById("img_src_28_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img14").hidden = true;
                document.getElementById("img14_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            } else if (num === 15) {
                let canvasSize1 = this.$refs.tuiImageEditor14.invoke('getCanvasSize');
                let url1 = this.$refs.tuiImageEditor14.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize1.width,
                    height: canvasSize1.height
                });
                let canvasSize2 = this.$refs.tuiImageEditor14_.invoke('getCanvasSize');
                let url2 = this.$refs.tuiImageEditor14_.invoke('toDataURL', {
                    left: 0,
                    top: 0,
                    width: canvasSize2.width,
                    height: canvasSize2.height
                });
                document.getElementById("img_src_29").src = url1;
                document.getElementById("img_src_30").src = url2;

                document.getElementById("img_src_29_preview").src = url1;
                document.getElementById("img_src_30_preview").src = url2;

                document.getElementById("div_img").hidden = true;
                document.getElementById("img15").hidden = true;
                document.getElementById("img15_first").hidden = false;
                document.getElementById("div_img_first").hidden = false;
            }
        }, async printThis(page) {
            this.downloading = true;
            console.log("printing..");
            let el = null;
            if (page === 1) {
                el = this.$refs.printcontent0;
            } else if (page === 2) {
                el = this.$refs.printcontent1;
            } else if (page === 3) {
                el = this.$refs.printcontent2;
            } else if (page === 4) {
                el = this.$refs.printcontent3;
            } else if (page === 5) {
                el = this.$refs.printcontent4;
            } else if (page === 6) {
                el = this.$refs.printcontent5;
            } else if (page === 7) {
                el = this.$refs.printcontent6;
            } else if (page === 8) {
                el = this.$refs.printcontent7;
            } else if (page === 9) {
                el = this.$refs.printcontent8;
            } else if (page === 10) {
                el = this.$refs.printcontent9;
            } else if (page === 11) {
                el = this.$refs.printcontent10;
            } else if (page === 12) {
                el = this.$refs.printcontent11;
            } else if (page === 13) {
                el = this.$refs.printcontent12;
            } else if (page === 14) {
                el = this.$refs.printcontent13;
            } else if (page === 15) {
                el = this.$refs.printcontent14;
            }


            const options = {
                type: "dataURL",
            };
            const printCanvas = await html2canvas(el, options);

            const link = document.createElement("a");
            link.setAttribute("download", "result.png");
            link.setAttribute(
                "href",
                printCanvas
                    .toDataURL("image/png")
                    .replace("image/png", "image/octet-stream")
            );
            link.click();

            setTimeout(() => {
                // Set downloading state back to false
                this.downloading = false
            }, 5000)

            console.log("done");

        }, async printThis_preview(page) {
            console.log("printing..");
            let el = null;
            if (page === 1) {
                el = this.$refs.printcontent0_preview;
            } else if (page === 2) {
                el = this.$refs.printcontent1_preview;
            } else if (page === 3) {
                el = this.$refs.printcontent2_preview;
            } else if (page === 4) {
                el = this.$refs.printcontent3_preview;
            } else if (page === 5) {
                el = this.$refs.printcontent4_preview;
            } else if (page === 6) {
                el = this.$refs.printcontent5_preview;
            } else if (page === 7) {
                el = this.$refs.printcontent6_preview;
            } else if (page === 8) {
                el = this.$refs.printcontent7_preview;
            } else if (page === 9) {
                el = this.$refs.printcontent8_preview;
            } else if (page === 10) {
                el = this.$refs.printcontent9_preview;
            } else if (page === 11) {
                el = this.$refs.printcontent10_preview;
            } else if (page === 12) {
                el = this.$refs.printcontent11_preview;
            } else if (page === 13) {
                el = this.$refs.printcontent12_preview;
            } else if (page === 14) {
                el = this.$refs.printcontent13_preview;
            } else if (page === 15) {
                el = this.$refs.printcontent14_preview;
            }


            const options = {
                type: "dataURL",
            };
            const printCanvas = await html2canvas(el, options);

            const link = document.createElement("a");
            link.setAttribute("download", "download.png");
            link.setAttribute(
                "href",
                printCanvas
                    .toDataURL("image/png")
                    .replace("image/png", "image/octet-stream")
            );
            link.click();

            console.log("done");
        }, async downloadAll() {
            let i = 1;
            let link1 = document.querySelectorAll("[id='url_image']");

            let objectLenght1 = Object.keys(link1).length;
            while (i <= objectLenght1 / 2) {
                await this.printThis(i);
                this.next_image_first(i);
                i++;
            }
            while (1 <= i) {
                this.back_image_first(i);
                i--;
            }
        }, preview(page) {

            document.getElementById("div_img_first_preview").hidden = false;
            document.getElementById("div_img_first").hidden = true;
            document.getElementById("btn_download_all").hidden = true;
            if (page === 1) {
                document.getElementById("img1_first_preview").hidden = false;
            } else if (page === 2) {
                document.getElementById("img2_first_preview").hidden = false;
            } else if (page === 3) {
                document.getElementById("img3_first_preview").hidden = false;
            } else if (page === 4) {
                document.getElementById("img4_first_preview").hidden = false;
            } else if (page === 5) {
                document.getElementById("img5_first_preview").hidden = false;
            } else if (page === 6) {
                document.getElementById("img6_first_preview").hidden = false;
            } else if (page === 7) {
                document.getElementById("img7_first_preview").hidden = false;
            } else if (page === 8) {
                document.getElementById("img8_first_preview").hidden = false;
            } else if (page === 9) {
                document.getElementById("img9_first_preview").hidden = false;
            } else if (page === 10) {
                document.getElementById("img10_first_preview").hidden = false;
            } else if (page === 11) {
                document.getElementById("img11_first_preview").hidden = false;
            } else if (page === 12) {
                document.getElementById("img12_first_preview").hidden = false;
            } else if (page === 13) {
                document.getElementById("img13_first_preview").hidden = false;
            } else if (page === 14) {
                document.getElementById("img14_first_preview").hidden = false;
            } else if (page === 15) {
                document.getElementById("img15_first_preview").hidden = false;
            }


        }, back_from_previwe() {
            document.getElementById("div_img_first_preview").hidden = true;
            document.getElementById("div_img_first").hidden = false;
            document.getElementById("btn_download_all").hidden = false;
        }, hide_all() {
            document.getElementById("img1").hidden = true;
            document.getElementById("img2").hidden = true;
            document.getElementById("img3").hidden = true;
            document.getElementById("img4").hidden = true;
            document.getElementById("img5").hidden = true;
            document.getElementById("img6").hidden = true;
            document.getElementById("img7").hidden = true;
            document.getElementById("img8").hidden = true;
            document.getElementById("img9").hidden = true;
            document.getElementById("img10").hidden = true;
            document.getElementById("img11").hidden = true;
            document.getElementById("img12").hidden = true;
            document.getElementById("img13").hidden = true;
            document.getElementById("img14").hidden = true;
            document.getElementById("img15").hidden = true;
            document.getElementById("img1_first").hidden = true;
            document.getElementById("img2_first").hidden = true;
            document.getElementById("img3_first").hidden = true;
            document.getElementById("img4_first").hidden = true;
            document.getElementById("img5_first").hidden = true;
            document.getElementById("img6_first").hidden = true;
            document.getElementById("img7_first").hidden = true;
            document.getElementById("img8_first").hidden = true;
            document.getElementById("img9_first").hidden = true;
            document.getElementById("img10_first").hidden = true;
            document.getElementById("img11_first").hidden = true;
            document.getElementById("img12_first").hidden = true;
            document.getElementById("img13_first").hidden = true;
            document.getElementById("img14_first").hidden = true;
            document.getElementById("img15_first").hidden = true;
            document.getElementById("img1_first_preview").hidden = true;
            document.getElementById("img2_first_preview").hidden = true;
            document.getElementById("img3_first_preview").hidden = true;
            document.getElementById("img4_first_preview").hidden = true;
            document.getElementById("img5_first_preview").hidden = true;
            document.getElementById("img6_first_preview").hidden = true;
            document.getElementById("img7_first_preview").hidden = true;
            document.getElementById("img8_first_preview").hidden = true;
            document.getElementById("img9_first_preview").hidden = true;
            document.getElementById("img10_first_preview").hidden = true;
            document.getElementById("img11_first_preview").hidden = true;
            document.getElementById("img12_first_preview").hidden = true;
            document.getElementById("img13_first_preview").hidden = true;
            document.getElementById("img14_first_preview").hidden = true;
            document.getElementById("img15_first_preview").hidden = true;
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