import { cn } from '@/lib/utils';
import Image from 'next/image';
import { buttonVariants } from '@/components/ui/button';
import { ArrowRight } from 'lucide-react';
import { SparklesText } from '@/components/ui/sparkles-text';
import Link from 'next/link';

export default function Home() {
  return (
    <>
      <div
        className='absolute inset-x-0 top-[360px] h-[250px]'
        style={{
          background: `
            repeating-linear-gradient(
              to right,
              color-mix(in oklab, var(--color-fd-primary) 10%, transparent),
              color-mix(in oklab, var(--color-fd-primary) 10%, transparent) 1px,
              transparent 1px,
              transparent 50px
            ),
            repeating-linear-gradient(
              to bottom,
              color-mix(in oklab, var(--color-fd-primary) 10%, transparent),
              color-mix(in oklab, var(--color-fd-primary) 10%, transparent) 1px,
              transparent 1px,
              transparent 50px
            )
          `,
        }}
      ></div>

      <main className='container relative max-w-[1100px] px-2 py-4 lg:py-8 min-h-screen sm:min-h-1'>
        <div className='relative'>
          <div className='relative flex flex-col border border-red-500/10 bg-fd-background/70 backdrop-blur-md px-4 pt-12 max-md:text-center md:px-12 md:pt-16 rounded-xl shadow-xl shadow-red-500/5 items-start justify-start'>
            <div
              className='absolute inset-0 z-0 top-1/5 blur-2xl hidden dark:block'
              style={{
                maskImage: 'linear-gradient(to bottom, transparent, white, transparent)',
                background:
                  'repeating-linear-gradient(65deg, var(--primary), var(--primary) 12px, color-mix(in oklab, var(--primary) 30%, transparent) 20px, transparent 200px)',
              }}
            />
            <div
              className='absolute text-left inset-0 z-0 top-1/5 blur-2xl dark:hidden'
              style={{
                maskImage: 'linear-gradient(to bottom, transparent, white, transparent)',
                background:
                  'repeating-linear-gradient(65deg, var(--primary), var(--primary) 12px, color-mix(in oklab, var(--primary) 30%, transparent) 20px, transparent 200px)',
              }}
            />
            <h1 className='mb-4 flex flex-wrap gap-2 text-3xl md:text-5xl font-medium leading-tight'>
              掌握{' '}
              <SparklesText
                colors={{
                  first: '#ed5ade',
                  second: '#5aedda',
                }}
              >
                STM32 嵌入式开发
              </SparklesText>{' '}
            </h1>
            <p className='mb-8 text-left text-muted-foreground md:max-w-[80%] md:text-xl'>
              本文档是一个系统化学习STM32嵌入式开发的平台，涵盖从入门基础到高级应用开发的全套内容。从芯片介绍、GPIO控制到各种外设驱动，配有详细示例与可视化讲解，助你全面提升嵌入式开发能力。
            </p>
            <div className='flex flex-wrap gap-4 mb-6 md:flex-row'>
              <div className='flex items-center gap-2'>
                <svg
                  className='w-5 h-5 text-red-500'
                  fill='none'
                  stroke='currentColor'
                  viewBox='0 0 24 24'
                  xmlns='http://www.w3.org/2000/svg'
                >
                  <path strokeLinecap='round' strokeLinejoin='round' strokeWidth='2' d='M5 13l4 4L19 7'></path>
                </svg>
                <span>GPIO 控制</span>
              </div>
              <div className='flex items-center gap-2'>
                <svg
                  className='w-5 h-5 text-red-500'
                  fill='none'
                  stroke='currentColor'
                  viewBox='0 0 24 24'
                  xmlns='http://www.w3.org/2000/svg'
                >
                  <path strokeLinecap='round' strokeLinejoin='round' strokeWidth='2' d='M5 13l4 4L19 7'></path>
                </svg>
                <span>外设驱动开发</span>
              </div>
              <div className='flex items-center gap-2'>
                <svg
                  className='w-5 h-5 text-red-500'
                  fill='none'
                  stroke='currentColor'
                  viewBox='0 0 24 24'
                  xmlns='http://www.w3.org/2000/svg'
                >
                  <path strokeLinecap='round' strokeLinejoin='round' strokeWidth='2' d='M5 13l4 4L19 7'></path>
                </svg>
                <span>标准库开发</span>
              </div>
              <div className='flex items-center gap-2'>
                <svg
                  className='w-5 h-5 text-red-500'
                  fill='none'
                  stroke='currentColor'
                  viewBox='0 0 24 24'
                  xmlns='http://www.w3.org/2000/svg'
                >
                  <path strokeLinecap='round' strokeLinejoin='round' strokeWidth='2' d='M5 13l4 4L19 7'></path>
                </svg>
                <span>实战项目应用</span>
              </div>
            </div>

            <div className='inline-flex justify-start z-10 mt-2 items-center gap-3'>
              <Link
                href='/docs/jxkj-stm32/std-start'
                className={cn(
                  buttonVariants({
                    size: 'lg',
                    className: 'from-primary to-primary/80 text-primary-foreground rounded-full bg-gradient-to-b',
                  })
                )}
              >
                开始学习 <ArrowRight className='size-4' />
              </Link>
              <Link
                href='/docs/std/introduction'
                className={cn(
                  buttonVariants({
                    size: 'lg',
                    variant: 'outline',
                    className: 'bg-background rounded-full',
                  })
                )}
              >
                标准库文档
              </Link>
            </div>

            <div className='relative mt-16 z-10 w-full'>
              <Image
                src='/cover.png'
                alt='STM32嵌入式开发文档预览'
                width={1000}
                height={800}
                priority
                className='w-full select-none duration-1000 animate-in fade-in -mb-60 slide-in-from-bottom-12 z-10 lg:-mb-40 rounded-lg mx-auto object-cover border-6 border-neutral-100 dark:border-neutral-600 shadow-2xl'
              />

              {/* Floating badges */}
              <div className='absolute -top-6 -right-6 bg-white dark:bg-neutral-900 rounded-lg shadow-lg p-3 rotate-9 transform animate-in fade-in slide-in-from-left-4'>
                <div className='flex items-center gap-2'>
                  <svg className='w-5 h-5 text-red-500' fill='currentColor' viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'>
                    <path
                      fillRule='evenodd'
                      d='M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z'
                      clipRule='evenodd'
                    ></path>
                  </svg>
                  <span className='font-medium'>STM32 实战教程</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </>
  );
}
