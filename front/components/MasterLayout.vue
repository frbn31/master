<template>
    <Layout>
        <template #navbar>
			<div class="flex w-full h-full bg-cyan-800 text-neutral-50">
				<NuxtLink class="flex items-center justify-center h-full w-fit p-2 font-sans" to="/apps/">Apps</NuxtLink>
				<NuxtLink class="flex items-center justify-center h-full w-fit p-2 font-sans" to="/stock/">Мастер</NuxtLink>
				<Dropdown group="0" class=" z-10 flex items-center justify-center h-full w-fit p-2 font-sans">
					<template #folded>
						<button class="flex items-center justify-center h-full w-fit p-2 font-sans">Продукт</button>
					</template>
					<NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/master/product/category/">Категории</NuxtLink>
					<NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/master/product/">Продукты</NuxtLink>
					<NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/master/bom/">Ведомости материалов</NuxtLink>
					<NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/master/product/lot/">ПН/СН</NuxtLink>
					<NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/master/uom/">ЕИ</NuxtLink>
				</Dropdown>
				<Dropdown group="0" class=" z-10 flex items-center justify-center h-full w-fit p-2 font-sans">
					<template #folded>
						<button class="flex items-center justify-center h-full w-fit p-2 font-sans">Склад</button>
					</template>
					<NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/master/stock/">Склады</NuxtLink>
					<NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/master/stock/operationtype/">Типы операций</NuxtLink>
					<NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/master/stock/distributionscheme/">Схемы распределений</NuxtLink>
				</Dropdown>
				<Dropdown group="0" class=" z-10 flex items-center justify-center h-full w-fit p-2 font-sans">
					<template #folded>
						<button class="flex items-center justify-center h-full w-fit p-2 font-sans">Компания</button>
					</template>
					<NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/master/company/department/">Подразделения</NuxtLink>
				</Dropdown>
			</div>
		</template>
      <slot />
    </Layout>
  </template>