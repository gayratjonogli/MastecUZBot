import asyncio
import aioschedule as schedule
from .messages import whiteMasterbatch, ufStabilizator, colorfulmasterbatch, organic_pigments, opticwhitener
from .specialGroups import opticwhitenerSPECIAL, ufStabilizatorSPECIAL, colorfulmasterbatchSPECIAL, \
    organic_pigmentsSPECIAL, whiteMasterbatchSPECIAL

from .aloneGroup import opticwhitenerAlone, ufStabilizatorAlone, colorfulmasterbatchAlone, organic_pigmentsAlone, \
    whiteMasterbatchAlone
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()


async def scheduled_job1():
    await whiteMasterbatch()


async def scheduled_job2():
    await colorfulmasterbatch()


async def scheduled_job3():
    await ufStabilizator()


async def scheduled_job4():
    await organic_pigments()


async def scheduled_job5():
    await opticwhitener()


#######################################
async def special1():
    await opticwhitenerSPECIAL()


async def special2():
    await ufStabilizatorSPECIAL()


async def special3():
    await colorfulmasterbatchSPECIAL()


async def special4():
    await organic_pigmentsSPECIAL()


async def special5():
    await whiteMasterbatchSPECIAL()


async def alone1():
    await organic_pigmentsAlone()


async def alone2():
    await opticwhitenerAlone()


async def alone3():
    await whiteMasterbatchAlone()


async def alone4():
    await ufStabilizatorAlone()


async def alone5():
    await colorfulmasterbatchAlone()


async def alone6():
    await organic_pigmentsAlone()


def start_scheduler():
    scheduler.add_job(scheduled_job1, 'cron', day_of_week='*', hour=9, minute=30)
    scheduler.add_job(scheduled_job2, 'cron', day_of_week='*', hour=9, minute=30)
    scheduler.add_job(scheduled_job3, 'cron', day_of_week='*', hour=9, minute=30)
    scheduler.add_job(scheduled_job4, 'cron', day_of_week='*', hour=9, minute=30)
    scheduler.add_job(scheduled_job5, 'cron', day_of_week='*', hour=9, minute=30)
    #############################################################################
    scheduler.add_job(scheduled_job1, 'cron', day_of_week='*', hour=12, minute=30)
    scheduler.add_job(scheduled_job2, 'cron', day_of_week='*', hour=12, minute=30)
    scheduler.add_job(scheduled_job3, 'cron', day_of_week='*', hour=12, minute=30)
    scheduler.add_job(scheduled_job4, 'cron', day_of_week='*', hour=12, minute=30)
    scheduler.add_job(scheduled_job5, 'cron', day_of_week='*', hour=12, minute=30)
    #############################################################################
    scheduler.add_job(scheduled_job1, 'cron', day_of_week='*', hour=17, minute=00)
    scheduler.add_job(scheduled_job2, 'cron', day_of_week='*', hour=17, minute=00)
    scheduler.add_job(scheduled_job3, 'cron', day_of_week='*', hour=17, minute=00)
    scheduler.add_job(scheduled_job4, 'cron', day_of_week='*', hour=17, minute=00)
    scheduler.add_job(scheduled_job5, 'cron', day_of_week='*', hour=17, minute=00)
    #############################################################################
    #############################################################################
    #############################################################################
    scheduler.add_job(alone1, 'cron', day_of_week='0', hour=9, minute=30)
    scheduler.add_job(alone2, 'cron', day_of_week='1', hour=10, minute=30)
    scheduler.add_job(alone3, 'cron', day_of_week='2', hour=11, minute=30)
    scheduler.add_job(alone4, 'cron', day_of_week='3', hour=12, minute=30)
    scheduler.add_job(alone5, 'cron', day_of_week='4', hour=15, minute=30)
    scheduler.add_job(alone5, 'cron', day_of_week='5', hour=17, minute=00)
    #############################################################################
    #############################################################################
    #############################################################################
    scheduler.add_job(special4, 'cron', day_of_week='0', hour=9, minute=30)
    scheduler.add_job(special2, 'cron', day_of_week='1', hour=9, minute=30)
    scheduler.add_job(special1, 'cron', day_of_week='2', hour=9, minute=30)
    scheduler.add_job(special3, 'cron', day_of_week='3', hour=9, minute=30)
    scheduler.add_job(special4, 'cron', day_of_week='4', hour=9, minute=30)
    scheduler.add_job(special2, 'cron', day_of_week='5', hour=9, minute=30)

    scheduler.add_job(special5, 'cron', day_of_week='0', hour=17, minute=00)
    scheduler.add_job(special3, 'cron', day_of_week='1', hour=17, minute=00)
    scheduler.add_job(special1, 'cron', day_of_week='2', hour=17, minute=00)
    scheduler.add_job(special3, 'cron', day_of_week='3', hour=17, minute=00)
    scheduler.add_job(special5, 'cron', day_of_week='4', hour=17, minute=00)
    scheduler.add_job(special1, 'cron', day_of_week='5', hour=17, minute=00)


    scheduler.start()
